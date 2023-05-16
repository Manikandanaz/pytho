import logging
class lg:
    def sample(self):
        #create logger
        logger=logging.getLogger("loggingpyfile")
        #set level
        logger.setLevel(logging.DEBUG)
        #define consolehandler/filehandler
        ch=logging.StreamHandler()
        fh=logging.FileHandler("logfile","a")
        #create formatter
        formatr=logging.Formatter('%(asctime)s %(filename)s %(levelname)s %(message)s',datefmt='%Y-%m-%d %H:%M:%S,uuu')
        formatr1=logging.Formatter('{asctime} {created} {filename} {levelname} {message}',datefmt='%Y-%m-%d %H:%M:%S,uuu',style='{')
        #set formatter
        ch.setFormatter(formatr)
        fh.setFormatter(formatr1)
        #add formatter
        logger.addHandler(ch)
        logger.addHandler(fh)
        logger.debug("debug statements")
        logger.info("infp statements")
        logger.warning("war statements")
        logger.error("err statements")
        logger.critical("cri statements")
obj=lg()
obj.sample()