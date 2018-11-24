import pygame
from pygame import draw
import random

#定义结点类(蛇的身体由多个结点构成)
class Node:
	
	CELL=20							#定义结点大小(所有结点共有定义为类变量)
	#构造方法
	#定义成员变量x,y为结点的左上角坐标
	def __init__(self,x,y):
		self.x=x
		self.y=y

	#绘制结点
	def draw_node(self,screen,color):
		draw.rect(screen,(0,205,102),(self.x,self.y,self.CELL,self.CELL),0)
		draw.rect(screen,color,(self.x+3,self.y+3,self.CELL-6,self.CELL-6),0)


WIDTH=800
HEIGHT=600										#屏幕大小
ROW=HEIGHT//Node.CELL							#行数和列数
COLUMN=WIDTH//Node.CELL
	
class Snake:
	
	#构造方法初始化蛇身
	def __init__(self):
		self.__snake_body=list()						#蛇身为列表(存储结点)
		self.__direction='down'							#定义蛇移动的方向
		self.__state=True								#蛇的存活状态
		self.score=0									#记录分数
		
		for i in range(0,5):
			self.__snake_body.append(Node(i*Node.CELL+400,100))


	#蛇的移动
	def move(self):
		
		head=self.__snake_body[0];				#得到蛇头
		newHead=Node(0,0)						#新蛇头
		if self.__direction=='up':
			newHead.x=head.x
			newHead.y=head.y-Node.CELL
		elif self.__direction=='down':
			newHead.x=head.x
			newHead.y=head.y+Node.CELL
		elif self.__direction=='left':
			newHead.x=head.x-Node.CELL
			newHead.y=head.y
		elif self.__direction=='right':
			newHead.x=head.x+Node.CELL
			newHead.y=head.y
		
		self.__snake_body.insert(0,newHead)

		self.__state=not self.isDead()				#记录蛇的存活状态

	#获取蛇的状态
	def get_state(self):
		return self.__state

	#根据输入的键改变蛇的方向
	def update_direction(self,pressed_key):
		if pressed_key[pygame.K_w] and self.__direction!='down':
				self.__direction='up'
		elif pressed_key[pygame.K_s] and self.__direction!='up':
				self.__direction='down'
		elif pressed_key[pygame.K_a]and self.__direction!='right':
				self.__direction='left'
		elif pressed_key[pygame.K_d] and self.__direction!='left':
				self.__direction='right'

	#判断蛇是否死亡
	def isDead(self):
		head=self.__snake_body[0]

		if head.x<0 or head.x>=WIDTH or head.y<0 or head.y>=HEIGHT:
			return True

		for i in range(1,len(self.__snake_body)):
			if head.x==self.__snake_body[i].x and head.y==self.__snake_body[i].y:
				return True

		return False


	#绘制蛇身
	def draw_snake(self,screen):
		self.__snake_body[0].draw_node(screen,(0,0,255))
		for i in range(1,len(self.__snake_body)):
			self.__snake_body[i].draw_node(screen,(0,255,127))

	#坐标是否与蛇身重叠
	def is_vailid(self,x,y):
		
		for node in self.__snake_body:
			if node.x==x and node.y==y:
				return True 
		return False

	#蛇吃食物
	def eat_food(self,food):
		head=self.__snake_body[0]

		if food.node.x==head.x and food.node.y==head.y:
			self.score+=1
			return True
		self.__snake_body.pop()						#没吃到删除蛇尾
		return False

#定义食物类
class Food:
	
	def __init__(self):
		self.node=Node(0,0)

	#根据蛇来随机产生食物
	def random_display(self,snake):
		x=random.randint(0,COLUMN-1)*Node.CELL
		y=random.randint(0,ROW-1)*Node.CELL

		while snake.is_vailid(x,y):
			x=random.randint(0,COLUMN-1)*Node.CELL
			y=random.randint(0,ROW-1)*Node.CELL
		self.node=Node(x,y)
	
	#画食物
	def draw_food(self,screen):
		self.node.draw_node(screen,(255,0,0))