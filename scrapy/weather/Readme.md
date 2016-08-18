pyv8 engine to parse js

# -*- coding:utf-8 -*-
import os,sys
import time
import json
from pyv8 import PyV8
import json
str = '''
{city:'济南',tqInfo:[{ymd:'2016-08-01',bWendu:'32℃',yWendu:'24℃',tianqi:'雷阵雨~多云',fengxiang:'北风',fengli:'1-2级',aqi:'47',aqiInfo:'优',aqiLevel:'1'},{ymd:'2016-08-02',bWendu:'31℃',yWendu:'23℃',tianqi:'多云',fengxiang:'北风',fengli:'1-2级',aqi:'94',aqiInfo:'良',aqiLevel:'2'},{ymd:'2016-08-03',bWendu:'31℃',yWendu:'24℃',tianqi:'晴~多云',fengxiang:'东北风',fengli:'1-2级',aqi:'112',aqiInfo:'轻度污染',aqiLevel:'3'},{ymd:'2016-08-04',bWendu:'31℃',yWendu:'24℃',tianqi:'雷阵雨~多云',fengxiang:'东风',fengli:'1-2级',aqi:'108',aqiInfo:'轻度污染',aqiLevel:'3'},{ymd:'2016-08-05',bWendu:'31℃',yWendu:'23℃',tianqi:'雷阵雨~多云',fengxiang:'南风',fengli:'1-2级',aqi:'79',aqiInfo:'良',aqiLevel:'2'},{ymd:'2016-08-06',bWendu:'31℃',yWendu:'23℃',tianqi:'雷阵雨',fengxiang:'东风',fengli:'1-2级',aqi:'71',aqiInfo:'良',aqiLevel:'2'},{ymd:'2016-08-07',bWendu:'28℃',yWendu:'23℃',tianqi:'中到大雨',fengxiang:'北风',fengli:'1-2级',aqi:'52',aqiInfo:'良',aqiLevel:'2'},{ymd:'2016-08-08',bWendu:'29℃',yWendu:'24℃',tianqi:'阵雨',fengxiang:'北风',fengli:'1-2级',aqi:'48',aqiInfo:'优',aqiLevel:'1'},{ymd:'2016-08-09',bWendu:'32℃',yWendu:'24℃',tianqi:'多云',fengxiang:'南风',fengli:'1-2级',aqi:'66',aqiInfo:'良',aqiLevel:'2'},{ymd:'2016-08-10',bWendu:'34℃',yWendu:'26℃',tianqi:'晴',fengxiang:'南风',fengli:'1-2级',aqi:'59',aqiInfo:'良',aqiLevel:'2'},{ymd:'2016-08-11',bWendu:'35℃',yWendu:'27℃',tianqi:'晴',fengxiang:'南风',fengli:'1-2级',aqi:'62',aqiInfo:'良',aqiLevel:'2'},{ymd:'2016-08-12',bWendu:'35℃',yWendu:'26℃',tianqi:'晴~多云',fengxiang:'南风',fengli:'1-2级',aqi:'59',aqiInfo:'良',aqiLevel:'2'},{ymd:'2016-08-13',bWendu:'34℃',yWendu:'25℃',tianqi:'多云~雷阵雨',fengxiang:'南风',fengli:'1-2级',aqi:'71',aqiInfo:'良',aqiLevel:'2'},{ymd:'2016-08-14',bWendu:'32℃',yWendu:'24℃',tianqi:'雷阵雨',fengxiang:'北风',fengli:'1-2级',aqi:'97',aqiInfo:'良',aqiLevel:'2'},{ymd:'2016-08-15',bWendu:'30℃',yWendu:'24℃',tianqi:'雷阵雨',fengxiang:'东北风',fengli:'1-2级',aqi:'77',aqiInfo:'良',aqiLevel:'2'},{ymd:'2016-08-16',bWendu:'27℃',yWendu:'23℃',tianqi:'雷阵雨',fengxiang:'北风',fengli:'1-2级',aqi:'50',aqiInfo:'优',aqiLevel:'1'},{ymd:'2016-08-17',bWendu:'28℃',yWendu:'23℃',tianqi:'中雨~多云',fengxiang:'东北风',fengli:'1-2级',aqi:'73',aqiInfo:'良',aqiLevel:'2'},{}],maxWendu:'35（2016-08-11）',minWendu:'23（2016-08-16）',avgbWendu:'31',avgyWendu:'24',maxAqi:'112',minAqi:'47',avgAqi:'72',maxAqiInfo:'轻度污染',maxAqiDate:'08月03日',maxAqiLevel:'3',minAqiInfo:'空气优',minAqiDate:'08月01日',minAqiLevel:'1'};

'''

def get_ctx():
    if not hasattr(get_ctx, 'ctx'):
        ctx = PyV8.JSContext()
        ctx.enter()
        get_ctx.ctx = ctx
    return get_ctx.ctx


def js2json(data):
    """ convert from javascript data
        to json data
    """
    ctx = PyV8.JSContext()
    ctx.enter()
    ctx.eval("""
            function func() {
              var data = """ + data + """;
              var json_data = JSON.stringify(data);
              return json_data;
            }
            """)

    jsond = ctx.locals.func()
    ctx.leave()
    return jsond


# jsond = js2json("{name: 'john',age: 10,}")
jsond = js2json(str)

print jsond

js = json.loads(jsond)
print js



class JSContext(pyv8._PyV8.JSContext)
 |  Method resolution order:
 |      JSContext
 |      pyv8._PyV8.JSContext
 |      Boost.Python.instance
 |      __builtin__.object
 |
 |  Methods defined here:
 |
 |  __enter__(self)
 |
 |  __exit__(self, exc_type, exc_value, traceback)
 |
 |  __init__(self, obj=None, extensions=[])
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from pyv8._PyV8.JSContext:
 |
 |  __nonzero__(...)
 |      __nonzero__( (JSContext)arg1) -> bool :
 |
 |          C++ signature :
 |              bool __nonzero__(CContext {lvalue})
 |
 |  __reduce__ = <unnamed Boost.Python function>(...)
 |
 |  enter(...)
 |      enter( (JSContext)arg1) -> None :
 |          Enter this context. After entering a context, all code compiled and run is compiled and run in this context.
 |
 |          C++ signature :
  |              void enter(CContext {lvalue})
 |
 |  eval(...)
 |      eval( (JSContext)arg1, (str)source [, (str)name='' [, (int)line=-1 [, (int)col=-1 [, (object)precompiled=None]]]]) -> object :
 |
 |          C++ signature :
 |              boost::python::api::object eval(CContext {lvalue},std::string [,std::string='' [,int=-1 [,int=-1 [,boost::python::api::object=None]]]])
 |
 |  leave(...)
 |      leave( (JSContext)arg1) -> None :
 |          Exit this context. Exiting the current context restores the context that was in place when entering the current context.
 |
 |          C++ signature :
 |              void leave(CContext {lvalue})
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from pyv8._PyV8.JSContext:
 |
 |  calling
 |
 |  current
 |
 |  entered
 |
 |  inContext
 |
 |  locals
 |      Local variables within context
 |
 |  securityToken
 |
 |  ----------------------------------------------------------------------
 |          Exit this context. Exiting the current context restores the context that was in place when entering the current context.
 |
 |          C++ signature :
 |              void leave(CContext {lvalue})
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from pyv8._PyV8.JSContext:
 |
 |  calling
 |
 |  current
 |
 |  entered
 |
 |  inContext
 |
 |  locals
 |      Local variables within context
 |
 |  securityToken
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from Boost.Python.instance:
 |
 |  __dict__
 |
 |  __weakref__
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes inherited from Boost.Python.instance:
 |
 |  __new__ = <built-in method __new__ of Boost.Python.class object>
 |      T.__new__(S, ...) -> a new object with type S, a subtype of T
(END)
