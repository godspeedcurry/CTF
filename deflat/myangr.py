import angr
import logging

logging.getLogger('angr').setLevel('INFO')   # 日志记录

proj = angr.Project("./StrangeInterpreter.recovered")  # 加载程序
state = proj.factory.entry_state()  #获取入口状态
state.posix.fd[0].size = 32
simgr = proj.factory.simgr(state)  #模拟

simgr.explore(find=0x412400, avoid=[0x412427, 0x4123B3]) # win 地址 和 lose的地址
print(simgr.found[0].posix.dumps(0))  打印答案
