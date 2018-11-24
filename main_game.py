import pygame							#导入pygame库
import sys
from pygame.locals import *
from pygame.color import THECOLORS		#导入颜色字典
from pygame import draw
from sanke_module import Snake
from sanke_module import Food


#定义窗口大小
SCREEN_WIDTH=800
SCREEM_HEIGHT=600
#获取pygame的时钟
fps_clock=pygame.time.Clock()

#绘制文字
def draw_text(screen,text,font_size,color,center_x,center_y):
	
	font=pygame.font.SysFont('华文楷体',font_size)
	text_surface=font.render(text,False,color)
	text_rect=text_surface.get_rect()
	text_rect.center=(center_x,center_y)
	screen.blit(text_surface,text_rect)


# 显示开始界面
def start_game(screen):
	title_Font = pygame.font.SysFont('华文楷体', 100)
	title_content = title_Font.render('贪吃蛇', True, (255,0,0), (0,255,0))
	angle = 0
	while True:
		screen.fill(THECOLORS['black'])
		rotated_title = pygame.transform.rotate(title_content, angle)
		rotated_title_Rect = rotated_title.get_rect()
		rotated_title_Rect.center = (SCREEN_WIDTH/2, SCREEM_HEIGHT/2)
		screen.blit(rotated_title, rotated_title_Rect)
		draw_text(screen,'按任意开始游戏',20,THECOLORS['white'],SCREEN_WIDTH/2,SCREEM_HEIGHT-40)
		
		for event in pygame.event.get():
			#判断事件类型退出游戏
			if event.type==QUIT:
				pygame.quit()
				sys.exit()
			elif event.type==KEYDOWN:
				return;

		pygame.display.update()
		fps_clock.tick(17)
		angle -= 5

def run_game(screen):
	#数据初始化
	eat_snake=Snake()
	food=Food()
	food.random_display(eat_snake)													#随机初始化食物的位置
	#游戏主循环(用于绘制画面和处理用户事件)
	fps=7;										#设施fps

	while True:
		if eat_snake.get_state():
			if	eat_snake.eat_food(food):
				food.random_display(eat_snake)		
			eat_snake.move()
			#绘制部分
			screen.fill((0,0,0))												#擦除原来的画面
			eat_snake.draw_snake(screen)
			food.draw_food(screen)
			draw_text(screen,'分数 '+str(eat_snake.score),20,THECOLORS['white'],SCREEN_WIDTH-50,20)
			
			if eat_snake.score%12==1:
				fps+=0.1
			#从事件列表中取出事件进行处理
			#处理游戏退出
			for event in pygame.event.get():
				#判断事件类型退出游戏
				if event.type==QUIT:
					pygame.quit()
					sys.exit()
			eat_snake.update_direction(pygame.key.get_pressed())

			pygame.display.update()
			#设置pygame的事件间隔
			fps_clock.tick(fps)
		else:
			return;																#蛇死亡退出游戏	

#游戏结束处理
def end_game(screen):
	
	#绘制结束文字
	draw_text(screen,'游戏结束',80,THECOLORS['red'],SCREEN_WIDTH/2,SCREEM_HEIGHT/2)
	draw_text(screen,'按任意键重新开始',30,THECOLORS['white'],SCREEN_WIDTH/2,SCREEM_HEIGHT/2+100)
	while True:
		for event in pygame.event.get():
				#判断事件类型退出游戏
				if event.type==QUIT:
					pygame.quit()
					sys.exit()
				elif event.type==KEYDOWN:
					return;							#检测到右按键按下(退出结束画面)
		pygame.display.update()


#初始化游戏
pygame.init()
#初始化窗口(返回一个窗口对象)
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEM_HEIGHT))
#设置窗口标题
pygame.display.set_caption('贪吃蛇')
start_game(screen)
while True:
	run_game(screen)
	end_game(screen)