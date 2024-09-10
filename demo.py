import ledscreen as led
import random, math


class Blob:
    def __init__(self,x,y, colour):
        self.x = x
        self.y = y
        self.angle = random.random()*2*math.pi
        self.speed = 2 + random.random()*3
        self.size = 5
        self.colour = colour
        self.xspeed = self.speed * math.cos(self.angle)
        self.yspeed = self.speed * math.sin(self.angle)
        self.pixels = {}

    def move(self):
        self.x = int((self.x + self.xspeed)) % 64
        self.y = int((self.y + self.yspeed)) % 64
        newpixels = {}
        for row in range(self.y-self.size, self.y + self.size + 1):
            for col in range(self.x - self.size, self.x + self.size + 1):
                # use pythagoras to calculate distance
                dist = math.sqrt(abs(self.y - row)**2 + abs(self.x-col)**2)
                if dist < self.size:
                    newpixels[row%64,col%64] = dist
                    led.drawPixel(row%64,col%64, self.colour)
        # erase old pixels
        for pixel in self.pixels:
            if pixel not in newpixels:
                led.drawPixel(pixel[0]%64,pixel[1]%64, [0,0,0])
        self.pixels = newpixels.copy()


blobs = []
for i in range(5):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    blobs.append(Blob(random.randint(0,64), random.randint(0,64), [r,g,b]))

while True:
    for b in blobs:
        b.move()
    led.refresh()
    led.tick(30)

