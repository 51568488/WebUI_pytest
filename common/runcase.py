def Run(env, browser, caselist):
    '''执行每个case文件的run_step()函数'''
    for index, text in enumerate(caselist):
        import_string = "src.case." + text
        mod= __import__(import_string, None, None, text, 0)  # import要执行的case模块
        mod.run_step(env, browser)  # 执行该模块的run_step()函数