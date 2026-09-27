"""Run a first browser-use task against the Hacker News front page."""

# 异步库：LLM、浏览器和代理的运行需要异步支持
import asyncio

# 读取环境变量
from dotenv import load_dotenv

# 这一步是关键了，导入我们自己封装的浏览器、代理和深度搜索模型
# 为啥能导入？因为整个文件作为包被pip到环境中了！
from browser_use import Agent, Browser, ChatDeepSeek

# async是异步函数的关键字，表示这个函数是异步的！！！
async def main() -> None:
	"""Ask the agent for the title of the top Hacker News story."""
	load_dotenv()

	# 创建一个agent实例！
	# Agent是一个类！
	agent = Agent(
		# task是任务描述！
		task='Open https://news.ycombinator.com/ and tell me the title of the #1 story.',
		llm=ChatDeepSeek(),
		# 选择浏览器，也是创建实例！
		# headless=False表示浏览器是可视化的，方便调试
		browser=Browser(channel='chrome', headless=False),
		# 这次不要主要依赖截图视觉能力
		# 后面学习Observation 时这个参数会比较有意思
		use_vision=False,
	)
	# awit 表示等待异步任务完成。最多十步！
	history = await agent.run(max_steps=10)
	print('最终结果：', history.final_result())


# 只有当这个文件被直接运行时，才执行下面代码
if __name__ == '__main__':
	asyncio.run(main())


# 上面的main函数是异步的，所以我们用asyncio.run来运行它
# 只是定义了一个main函数，所以需要在最后加上if __name__ == '__main__': asyncio.run(main())来运行它

# 为啥直接运行文件才执行函数内容？
# 不然的话，如果这个文件被其他文件import了，就会直接执行main函数，这样就不太好啦！