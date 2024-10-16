def startGame(game, vfps):
  game.start(vfps)
  program.start(game.arg1)

main()

def main():
  startGame("Minecraft", 60)
