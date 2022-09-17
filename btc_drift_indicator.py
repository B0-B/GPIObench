# url modules


'''
This is a useful script for crypto investments.
The script fetches OHLC data repeatedly, computes the logarithmic
returns allowing to compute the sample statistics like drift (mean) 
and volatility (standard deviation). If the drift is negative
the color indicates the magnitude (red via yellow to green = bearish, neutral, bullish)
and the pulsation rate will correlate with the volatility. 
'''

from urllib.error import HTTPError
from urllib.request import Request
import urllib.request as urllib2
import urllib.parse as urllib
from traceback import print_exc
from datetime import datetime, timedelta
from tools.rgb import RGBLED, stopRequested
import numpy as np
from time import sleep
import json

# ---- PARAMETERS ----
_coin = 'xbt'
_interval = 5   # minutes
_window = 144   # minutes
_expectedDriftPercentage = .01
_expectedVolPercentage = 0.3
_pins = (2,3,4)
_pulseMaxTime = 5       # seconds
_pulseMinTime = 0.5     # senconds
_greenCol = (0, 255, 0)
_neutralCol = (255, 230, 0)
_redCol = (255, 0, 0)
_update = 30    # seconds
# --------------------

def ohlc (coin, interval):

    '''
    Requests OHLC timeseries data 720 points of chosen time intervals in minutes.
    '''

    pair = f'{coin.upper()}USD'
    epoch = 720*interval
    data = {
        'pair' : pair,
        'interval' : interval,
        'since' : (datetime.now()-timedelta(minutes=epoch)).timestamp()
    }

    postdata = urllib.urlencode(data)
    body = postdata.encode('utf-8')
    try:
        request = Request('https://api.kraken.com/0/public/OHLC', data=body)
    except HTTPError:
        raise ConnectionError('lost connection to kraken API')
    except Exception as e:
        print_exc()

    ticket = urllib2.urlopen(request)
    raw_data = ticket.read()
    encoding = ticket.info().get_content_charset('utf8') # JSON default
    errors = json.loads(raw_data.decode(encoding))['error']  # return ticket result
    
    result = json.loads(raw_data.decode(encoding))['result']
    timeseries = result[list(result.keys())[0]]
    if 'EService:Busy' in errors:
        raise ConnectionAbortedError('kraken API service is busy')
    
    # extract closed prices
    c = []
    for v in timeseries:
        c.append(float(v[4]))

    return c

def IO (x):
    if x > 0:
        return 1
    return 0

def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))

def colorFade (x):

    return [255*(1-x), 255*x, 50*gaussian(x, .5, .1)]

    # c1 = np.array(_redCol)
    # c2 = np.array(_neutralCol)
    # c3 = np.array(_greenCol)

    # mixer = lambda x, mu, c: gaussian(x, mu, .3) * c

    # r = mixer(x, 0, c1)
    # y = mixer(x, .5, c2)
    # g = mixer(x, 1, c3)

    # col = r + y + g

    # print('col', col)

    # for i in range(3):
    #     col[i] = np.min([255, col[i]])
    # print('col', col)
    #return col

def main ():

    '''
    Main program.
    '''

    # load LED object
    LED = RGBLED(*_pins)
    LED.on()

    color = _neutralCol
    LED.color(*color)

    f_min = 1/_pulseMaxTime
    f_max = 1/_pulseMinTime
    
    while not stopRequested():
        
        try:

            # request OHLC data and crop to recent window
            data = ohlc(_coin, _interval)[-_window:]
            
            # compute statistics in percent
            drifts = [np.log(data[i+1]/data[i]) for i in range(len(data)-1)]
            drift = np.mean(drifts)*100
            vol = np.std(drifts)*100
            #print(drift, vol)

            # set LED dynamics using expectation and a sigmoid activation function
            freq = (f_max-f_min)/(1+np.sqrt(-vol/_expectedVolPercentage)) + f_min
            mag = 1/(1+np.exp(-drift/_expectedDriftPercentage))

            print('mag', mag)
            
            # combine magnitude to alter the color strength
            col = colorFade(mag)

            # apply settings to LED
            #LED.pulse(color=col, frequency=freq, duration=_update)
            LED.transition(color, col)
            color = col
            sleep(_update)

        except KeyboardInterrupt:

            LED.stop()
            quit()

        except:

            print_exc()
        


if __name__ == '__main__':
    main()