import os
import time
import nonebot
import psutil
from datetime import datetime
from random import randint, choice
from pathlib import Path

import config # type: ignore


bot = nonebot.get_bot()
master = config.MASTER()


@nonebot.scheduler.scheduled_job(
    'cron',
    hour = 7,
    misfire_grace_time= 60
)
async def _():
    """早安"""
    try:
        await bot.send_private_msg(user_id = master, message = f'ATRI将在三秒后开始执行定时任务：早安') # type: ignore
        time.sleep(3)
        start = time.perf_counter()
        group_list = await bot.get_group_list() #type: ignore
        groups = [group['group_id'] for group in group_list]
        g_list = len(group_list)
        msg = choice(
            [
                '啊......早上好...(哈欠)',
                '唔......吧唧...早上...哈啊啊~~~\n早上好......',
                '早上好......',
                '早上好呜......呼啊啊~~~~',
                '啊......早上好。\n昨晚也很激情呢！',
                '吧唧吧唧......怎么了...已经早上了么...',
                '早上好！',
                '......看起来像是傍晚，其实已经早上了吗？',
                '早上好......欸~~~脸好近呢'
                '......(打瞌睡)',
            ]
        )

        try:
            for group in groups:
                time.sleep(randint(1,5))
                await bot.send_group_msg(group_id = group, message = msg) #type: ignore
        except:
            await bot.send_private_msg(user_id = master, message = f'在推送[早安]到某些群的时候貌似失败了呢') # type: ignore

        end = time.perf_counter()
        await bot.send_private_msg(user_id = master, message = f'已推送到[{g_list}]个群\n耗时：{round(end - start, 3)}') # type: ignore

    except:
        pass

@nonebot.scheduler.scheduled_job(
    'cron',
    hour = 22,
    misfire_grace_time = 60
)
async def _():
    """晚安"""
    try:
        await bot.send_private_msg(user_id = master, message = f'ATRI将在三秒后开始执行定时任务：晚安') # type: ignore
        time.sleep(3)
        start = time.perf_counter()
        group_list = await bot.get_group_list() #type: ignore
        groups = [group['group_id'] for group in group_list]
        g_list = len(group_list)
        msg = choice(
            [
                '忙累了一天，快休息吧',
                '辛苦了一天，准备睡觉吧',
                '一起睡觉吧~~~~~',
                '......该睡觉了',
                '还不睡等着猝死？嗯！？'

            ]
        )

        try:
            for group in groups:
                time.sleep(randint(1,5))
                await bot.send_group_msg(group_id = group, message = msg) #type: ignore
        except:
            await bot.send_private_msg(user_id = master, message = f'在推送[晚安]到某些群的时候貌似失败了呢') # type: ignore
        
        end = time.perf_counter()
        await bot.send_private_msg(user_id = master, message = f'已推送到[{g_list}]个群\n耗时：{round(end - start, 3)}') # type: ignore
    
    except:
        pass

@nonebot.scheduler.scheduled_job(
    'cron',
    hour = 24,
    misfire_grace_time = 60
)
async def _():
    """到 点 了"""
    try:
        await bot.send_private_msg(user_id = master, message = f'ATRI将在三秒后开始执行定时任务：网抑云') # type: ignore
        time.sleep(3)
        start = time.perf_counter()
        group_list = await bot.get_group_list() # type: ignore
        groups = [group['group_id'] for group in group_list]
        g_list = len(group_list)
        msg = f'到点了叻~！'

        try:
            for group in groups:
                time.sleep(randint(1,5))
                await bot.send_group_msg(group_id = group, message = msg) #type: ignore
        except:
            await bot.send_private_msg(user_id = master, message = f'在推送[网抑云]到某些群的时候貌似失败了呢') # type: ignore
        
        end = time.perf_counter()
        await bot.send_private_msg(user_id = master, message = f'已推送到[{g_list}]个群\n耗时：{round(end - start, 3)}') # type: ignore

    except:
        pass

@nonebot.scheduler.scheduled_job(
    'interval',
    minutes = 5,
    misfire_grace_time= 10
)
async def _():
    print('ATRI开始自检...')
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    today = datetime.now()

    if cpu > 80:
        await bot.send_private_msg(
            user_id = master,
            message = f'ATRI感觉头有点晕...\n（cpu:{cpu}% mem:{memory}% disk:{disk}%）\n{today}'
        ) # type: ignore
    
    elif memory > 80:
        await bot.send_private_msg(
            user_id = master,
            message = f'ATRI感觉身体有点累...\n（cpu:{cpu}% mem:{memory}% disk:{disk}%）\n{today}'
        ) # type: ignore
    
    elif disk > 80:
        await bot.send_private_msg(
            user_id = master,
            message = f'ATRI感觉身体要被塞满了...\n（cpu:{cpu}% mem:{memory}% disk:{disk}%）\n{today}'
        ) # type: ignore
    
    else:
        print('ATRI运作正常！')