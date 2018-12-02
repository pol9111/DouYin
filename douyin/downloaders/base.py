from tqdm import tqdm
import asyncio
import math
import types


class Downloader(object):
    
    def __init__(self, handlers=[], batch=10):
        """
        init attributes
        :param handlers:
        """
        self.handlers = handlers # 空列表, 接受headler
        self.batch = batch # 一组10个
    
    def add_handler(self, handler):
        """
        add one handler
        :param handler: handler object
        :return:
        """
        self.handlers.append(handler) # 往handler列表添加
    
    def set_handlers(self, handlers):
        """
        set handlers
        :param handlers:
        :return:
        """
        self.handlers = handlers
    
    def get_handlers(self):
        """
        get handlers of downloader
        :return:
        """
        return self.handlers
    
    def update_progress(self, _):
        """
        update progress bar
        :return:
        """
        self.bar.update(1)
    
    async def process_item(self, obj):
        """
        process item
        :param obj: single obj
        :return:
        """
        raise NotImplementedError
    
    def process_items(self, objs):
        """
        process items
        :param objs: objs
        :return:
        """
        # define progress bar
        with tqdm(total=len(objs)) as self.bar:
            # init event loop
            loop = asyncio.get_event_loop()
            # get num of batches 有几组, batch=10
            total_step = int(math.ceil(len(objs) / self.batch)) # math.ceil向上取整
            # for every batch
            for step in range(total_step):
                start, end = step * self.batch, (step + 1) * self.batch
                print('Processing %d-%d of files' % (start + 1, end))
                # get batch of objs
                objs_batch = objs[start: end] # 指定一组只有10个
                # define tasks and run loop  process_item执行异步下载
                tasks = [asyncio.ensure_future(self.process_item(obj)) for obj in objs_batch]
                for task in tasks: # 更新进度条
                    task.add_done_callback(self.update_progress)
                loop.run_until_complete(asyncio.wait(tasks))
    
    def download(self, inputs):
        """
        download video or video lists
        :param data:
        :return:
        """
        if isinstance(inputs, types.GeneratorType):
            temps = []
            for result in inputs:
                print('Processing', result, '...')
                temps.append(result)
                if len(temps) == self.batch: # 每10个一组
                    self.process_items(temps)
                    temps = [] # 清空temps
        else:
            inputs = inputs if isinstance(inputs, list) else [inputs] # 把input变成list
            self.process_items(inputs)
