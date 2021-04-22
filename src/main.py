from TwitterAnalysis.TwitterProducer import TwitterProducer
from TwitterAnalysis.TwitterConsumer import TwitterConsumer
from multiprocessing import Process

def ProducerTweetsData():
  twitter_producer = TwitterProducer('computer-science')
  twitter_producer.CollectTweets

def ConsumeTweetsData():
  twitter_consumer = TwitterConsumer('computer-science')
  twitter_consumer.ConsumerTweets

if __name__ == '__main__':
  
  def runInParallel(*fns):
    proc = []
    for fn in fns:
      process = Process(target=fn)
      process.start()
      proc.append(process)
    for p in proc:
      p.join()
    
  runInParallel(ProducerTweetsData, ConsumeTweetsData)
      
  
        
        
    