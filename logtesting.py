import logging

log = logging.getLogger('logtesting')
log.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(levelname)s] %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
log.addHandler(handler)
handler_file = logging.FileHandler('plane.log')
handler_file.setFormatter(formatter)
log.addHandler(handler_file)

def test():
	log.debug("Debug here")
	log.info('info here')
	log.warn('warning here')
	log.error('error here')
	log.critical('critical here')
	
test()