import logging
import logging.config
import os
class lg:
    def sample(self):
        #create logger
        logger=os.path.join(os.getcwd(),'dictlog.conf')
        
        logging.config.fileConfig(logger)
        logger=logging.getLogger("mylogger")
        logger.debug("Unexpected:{}".format(os.getcwd()),extra= {'clientip': '192.168.0.1', 'user': 'fbloggs'})
       # logger.info("Unexpected:{}".format(os.getcwd()),extra= {'clientip': '192.168.0.1', 'user': 'info'})
       
obj=lg()
obj.sample()