import pygame
import sys

# 全局初始化
pygame.init()
# 音效初始化
pygame.mixer.init()
# 设置窗口大小
resolution = width, height = 900, 300
# 设置全局分辨率
windowSurface = pygame.display.set_mode(resolution)
# 设置标题
pygame.display.set_caption("Dino")
# 设置图标
icon = pygame.image.load("./material/picture/icon.png")
pygame.display.set_icon(icon)
# 加载背景图

# 背景音乐
pygame.mixer.music.load("./material/sound/背景音效2.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.4)

# 创建时钟对象
clock = pygame.time.Clock()


if __name__ == "__main__":
    # 开启消息循环
    while True:
        # 事件处理
        for event in pygame.event.get():
            # 处理退出事件
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # 绘制背景
        windowSurface.fill((255, 255, 255))

        # 刷新界面
        pygame.display.flip()

        # 时钟停留1帧
        clock.tick(60)
