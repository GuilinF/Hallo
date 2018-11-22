"""
Reinforcement learning maze example.
Red rectangle:          explorer.
Black rectangles:       hells       [reward = -1].
Yellow bin circle:      paradise    [reward = +1].
All other states:       ground      [reward = 0].
This script is the main part which controls the update method of this example.
The RL is in RL_brain.py.
View more on my tutorial page: https://morvanzhou.github.io/tutorials/
"""

from maze_env import Maze
from RL_brain import QLearningTable

"迭代更新部分"
def update():
    "对应运行100次"
    for episode in range(100):
        "对观测值进行初始化"
        # initial observation
        observation = env.reset()
        "while true在这里是什么意思？"
        while True:
            # fresh env,更新可视化环境
            env.render()

            # RL choose action based on observation，RL根据state的观测值挑选一个动作
            action = RL.choose_action(str(observation))

            # RL take action and get next observation and reward
            #探索者实行这个动作，根据动作得出下一个状态、回报和是否是升上天空或者掉入地狱
            observation_, reward, done = env.step(action)

            # RL learn from this transition
            #RL从这个序列state、action、reward、和接下来的state_中进行学习
            RL.learn(str(observation), action, reward, str(observation_))

            # swap observation，将观测值进行更新
            observation = observation_

            # break while loop when end of this episode，如果掉入地狱或者升上天空，这回合就结束了
            if done:
                break

    # end of game，结束游戏，并关闭窗口
    print('game over')
    env.destroy()

if __name__ == "__main__":
    #定义环境env和RL的方式
    env = Maze()
    RL = QLearningTable(actions=list(range(env.n_actions)))

    #开始可视化环境，这个地方不懂？
    env.after(100, update)
    env.mainloop()