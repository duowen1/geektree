# 第三届腾讯极客技术挑战赛WriteUp（JS零基础的大白话版）

期待了很久的第三届比赛终于来了，几天的时间“种了200W棵树”，我对自己的成绩还是比较满意的，尤其是考虑到自己还是一个web零基础而且都不知道js是什么的纯小白。本Writeup主要展示小白做题的心路历程，力求让像我一样啥都不懂的同学也能理解题目的含义、了解解题思路。我最大的梦想就是进入腾讯工作，虽然这一次没有拿到免面试资格，但我会继续努力的。

[比赛地址](http://geek.qq.com/tree/)

# 0-1w
第一题其实就是想告诉大家这个比赛是怎么玩的，进来先读题目说明：
> - 用现代浏览器
> - 禁止攻击比赛服务器
> - 1秒内种下多棵树，会触发加速buff
> - 几乎不需要写代码（我信你个大头鬼）

一个绿绿的按钮“点我开始种树”，然后三秒之后就种好了第一棵树。那么很显然没触发加速效果，虽然我还不知道未来会发生什么，但是冥冥之中想到F12看看按下按钮后发生了什么。

![todo]()

从“网络”选项卡中可以看出，手动点击按钮后有三次数据包。

都已经进入开发者模式了，不审查元素不合适吧，看一看网页到底执行了什么内容。

```js
todo
```

嵌入在html页面中的代码解释了为什么会有三次数据包：
1. 发送含有参数u的请求，服务器返回一段json格式的数据。
2. 发送含有参数c的请求，服务器返回一段js代码:
```js
window.A274075A=async function({a}){
    return new Promise(_=>setTimeout(__=>_(a[0]),2000))
}
```
3. 发送含有参数u和a的请求，种树成功。

至此，明白了题目1实际就是把第一次请求发来的a再发回服务器。等点击按钮整个过程长达三秒的原因就是因为代码中调用了setTimeout函数进行了延时。那我们可以手动构造数据包，直接向服务器发送请求。

当然可以选择使用浏览器开发者模式的命令行进行发送，但是对于我等小白来讲，没有什么比python更合适了，引入request和json包，随手撸一个代码，成功拿到1w分。

```js
while True:
    url = "http://159.75.70.9:8081/pull?u=uid"
    res=requests.get(url=url)
    d=json.loads(res.text)
    a0=d["a"]
    t=d["t"]
    url='http://159.75.70.9:8081/push?t=%s&a=%s'%(t,a0[0])
    res=requests.get(url=url)
    print(res.text)
```

[solve1.py](https://github.com/duowen1/geektree/blob/master/1.1w/solve1.py)

# 1w-10w
和第一题相比几乎没有任何的不同，只需要额外进行一次运算，唯一的要求就是能看懂js代码。至于零基础怎么看懂，没啥办法，百度呗。

查看第二次请求返回的js文件，发现对a进行了运算，只需要返回a*a+a即可。

[solve2.py](https://github.com/duowen1/geektree/blob/master/2.10w/solve2.py)

# 10w-25w
拿到手的是一大段经过base64编码的代码，解码后进行格式化。
```js
var _0xe936=['A5473788'];
(function(_0x48e85c,_0xe936d8){
    var _0x23fc5a=function(_0x2858d9){
        while(--_0x2858d9){
            _0x48e85c['push'](_0x48e85c['shift']());
        }
    };
    _0x23fc5a(++_0xe936d8);
}(_0xe936,0x196));
var _0x23fc=function(_0x48e85c,_0xe936d8){
    _0x48e85c=_0x48e85c-0x0;
    var _0x23fc5a=_0xe936[_0x48e85c];
    return _0x23fc5a;
};
window[_0x23fc('0x0')]=function(_0x335437){
    var _0x1aac02=0x30d3f;
    for(var _0x3bed6a=0x30d3f;_0x3bed6a>0x0;_0x3bed6a--){
        var _0x375340=0x0;
        for(var _0x1ddb77=0x0;_0x1ddb77<_0x3bed6a;_0x1ddb77++){
            _0x375340+=_0x335437['a'][0x0];
        }
        _0x375340%_0x335437['a'][0x2]==_0x335437['a'][0x1]&&_0x3bed6a<_0x1aac02&&(_0x1aac02=_0x3bed6a);
    }
    return _0x1aac02;
};
```

变量名经过了混淆，简单替换一下变量名，发现真正有意义的只有第三个函数：
```js
window[fun('0x0')]=function(arg){
    var temp=0x30d3f;
    for(var i=0x30d3f;i>0x0;i--){
        var m=0x0;
        for(var j=0x0;j<i;j++){
            m+=arg['a'][0x0];
        }
        m%arg['a'][0x2]==arg['a'][0x1]&&i<temp&&(temp=i);
    }
    return temp;
};
```

[solve3.py](https://github.com/duowen1/geektree/blob/master/3.25w/solve3.py)

# 25w-50w
直接看js文件，一大段神秘的符号直接把我晃瞎了。没错，就是jsfuck。

![jsfuck](https://github.com/duowen1/geektree/blob/master/4.50w/%E7%BD%91%E9%A1%B5%E6%8D%95%E8%8E%B7_24-3-2021_85415_159.75.70.9.jpeg)

## 解jsfuck
jsfuck详解可自行google

最简单的解jsfuck的方法就是使用浏览器自带的命令行功能，将jsfuck代码粘贴到命令行可以显示方便阅读的代码。

```javascript
window.A593C8B8=async(arg)=>(($,window,r,c,d)=>{
    let fun1=function*(){
        while([])
            yield[(a,b)=>a+b,(a,b)=>a-b,(a,b)=>a*b][++r%3]["bind"](0,c,d)
    }();
    let fun2=function(a,fun,res){
        d=a;
        c=fun["next"]()["value"]();
        r==window["a"]["length"]&&res(-c)
    };
    return new Promise(para=>window["a"]["foreach"](val=>$["setTimeout"](temp=>fun2(val,fun1,para),val)))
})(window,arg,0,0,0)
```

## 解后续
jsfuck还可以通过命令行进行解，但是后续的代码确实要求对js代码的理解有一定深度。这一关卡很难速成，所以我在这里面卡了很久。但是无论如何，我们还是可以通过静态分析和动态分析相结合的方式了解这段代码的含义。

### 静态分析
感谢vscode已经对代码进行了高亮，即使解了jusck，但是还是存在着变量名混淆，通过vscode的代码高亮可以帮助我们判断变量的作用域等。

### 动态分析


通过静态和动态两种方式，终于理解了代码含义。直接python实现上述逻辑，
[solve4.py](https://github.com/duowen1/geektree/blob/master/4.50w/solve4.py)

# 50w-100w
这一步开始手动点击按钮就出现了明显的时延，没有setTimeout，那么可以断定是算法本身的复杂度造成。
## 解wasm
其实这一步稍微搜集一下信息就能找到一个非常有名的工具：
[wasm2c](https://github.com/WebAssembly/wabt)

做题中的我对这段代码毫无兴趣，只考虑怎么把题目解出来，反正也没说不让使用开源工具，直接跑一下就可以得到一段类似于c语言的代码。

```js
function jwork5(v0,v1){
    let v2,v3,v4,v5,v6,v7;
    v2=v0;
    v4=v1-1;
    while(true){
        v3=v2;
        v6=0;
        v7=10;
        while(true){
            v5=v3%10;
            v3=Math.floor(v3/10);
            v6=Math.max(v5,v6);
            v7=Math.min(v5,v7);
            if(v3<=0) break;
        }
        v2=v6*v7+v2;
        v4=v4-1;
        if(v4<=0) break;
    }
    let result=v2;
    return result;
}
```


## 算法优化
用python实现上述算法，发现确实会运行很久，那么必须进行算法优化。首先先了解这段代码具体做了什么事情，实际上还是比较容易看明白的。内层循环获取这个数每一位上的最大值和最小值，相乘后和原来的数相加并开启下次循环，直到命中退出条件。

如果打印出中间结果，可以发现v2的值最后是不会变化的。那么可以确定v6*v7的结果是0，也就是说v6和v7中一个数值为0，那显然只能是最小值为0。可以得到一个结论，当v2中的某一位为0时，就已经得到了最终结果，直接返回即可。



[solve5.py](https://github.com/duowen1/geektree/blob/master/5.100w/solve5.py)

# 100w-200w
终于来到100w大关，此时的我现在有点自信心膨胀，于是信心满满的打开了js文件。首先对代码进行格式化，带有缩进的代码可以帮助快速读懂代码的逻辑。

[CA.js]()

在函数```__TENCENT_CHAOS_VM```中：
- ```f```是列表的索引：代码中```e[f++]```这样的表示式经常出现
- ```e```是列表，实际上也就是作为参数传递进来的```[33,3,25,2......]```，e中的元素既表示了要进行的操作，也表示了进行操作的数据。和计算机本身一样，代码和数据是不加区分地保存在内存中的。
- ```r```是栈，所有的操作都是在栈上做的，可以看到大量的类似于```r.pop(),r.push()```的代码

整个代码的流程就是不断通过索引f去取数组e中的数据，然后根据数据调用不同的函数，函数中会对栈r进行一定的操作，最终返回。

让我们继续观察一下代码：
在第130行：
```js
for(0;;)try{
    for(var p=!1;!p;) p=u[e[f++]]();
    if(0,o) throw o;
    return n?(r.pop(),r.slice(3+__TENCENT_CHAOS_VM.v)):r.pop()
}
```
在循环里，```p=u[e[f++]]()```，p接收一个函数的返回值。而这个函数在列表u中，通过e[f++]获取。u中的函数都是没有返回值的，也就是p应该为undefined，再取反为true，循环继续。除了一个函数，第31行的函数7：
```js
function(){
    return !0
}//函数7
```
然后true，再取反为false，所以循环退出。也就是说函数7肯定是退出函数，也就是这个虚拟机保护系统的出口。

## js虚拟机
通过静态分析得到了一些基本的认识，但是已经很难看出来代码更多具体的行为了，所以采用动态调试的方法。

在函数入口处下断点，除了可以获得函数参数的值以外，没有获得更多的有价值的信息。然后开启单步调式，多跟踪几步（实际上是几十步、几百步）看一看。

静态分析已经确定，有很多有关于栈的操作以及e[f++]，这指示了动态调试时应当关注的信息——栈r的变化，以及参数f的变化。

### 为什么f不是一直增加的
通过观察发现，f的值不是一直在增加的，有时会减少，然后再进入到增加的过程，并且彼此往复。那么可以确定，必定是调用了一些会对f的值直接修改的函数。

第54行，函数17：
```js
function(){
    f=e[f++]
}
```

第70行，函数32：
```javascript
funcion(){
    var n=e[f++];
    r[r.length-1]&&(f=n)
}
```
在这两个函数出下断点，发现每次促使```f```减少的正是函数32。正是由于```r[r.lenth-1]```为假才导致了f=n被执行。

然后经过若干次的单步调试，当然也可以结合一些技巧。技巧就是，关注那些可能改变执行流的函数，在一些存在比较、控制流分支的函数下断点。最终定位到函数34：

第78行，函数34
```js
function(){
    r[r.length-2]=r[r.length-2]>=r.pop()
}
```
函数34比较了栈上两个元素的值，并将true或者false放回栈顶。既然是这样那就看下栈顶上的两个元素是什么呗。凭借着对于参数的敏感，我一眼认出了栈顶的元素正式通过请求获得数组```["a"][0]```。那么栈顶上第二个元素是什么呢？

把其他断点都取消，只保留函数34的断点，让程序每次都在函数34中断。我们可以看到，每启动一次程序，栈顶上第二个元素就加一，然后去和栈顶元素进行比较。

上文提到，```f```的值是周期性变化的。那么通过这里的分析可以确定，数组```["a"][0]```正是控制循环次数用的。

那么下一步的工作就是去分析，这个循环里到底做了什么事情。

### 循环里到底运行了什么
这一部分算是最为复杂的部分，各种栈上的操作很容易把人看晕。但是有一个很特殊的函数引起了我的注意，也就是126行的函数68：

```js
function(){
    r[r.length-1]+=String.fromCharCode(e[f++])
}
```
这个函数从e中读取一个ascii码并转化成字符，这个函数多次被调用（可以发现e中有很多元素68）。多跟踪几次就能发现，读取到的数据是有规律的，“BigInt”、“1125899906842597”和一个7位数多次出现。然后在出现这些数字后进行单步调试，看看这些数在栈里面是如何变化的。

是比较容易定位到函数44和函数15的，可以总结出逻辑，上次的运算结果和7位数相乘，然后对1125899906842597取余数。

至此，循环里的操作终于明朗了，实际整体的操作就是计算7位数的a["a"][0]幂对1125899906842597的余数。【快速幂算法警告！！！】

### ```["a"][0]```解决了，```["a"][1:11]```还远吗？
到这里我已经相信后面的对a的操作应该大同小异，只要找到异在哪里，那么这道题就迎刃而解了。

为了分析后面的a，必须让第一个["a"][0]运行完毕再进行分析。那么怎么样才能让a运行完毕时程序能停住呢？**条件**断点看上去是个不错的选择（实际是个很差的选择）。

上文提到函数34是个特别的函数，他的执行结果直接影响了后面的执行流。如果在函数34放置一个条件断点，这样就可以控制程序执行的进度，可以直接让程序运行到["a"][0]循环的结束。然后再去动态分析["a"][1]以及后续的过程。

但是！这真的是一个不好的想法，因为条件断点会大大影响程序的执行速度，本来循环次数就很多，再加上条件断点，程序基本处于拒绝服务的状态。

那换种思路，有没有可能让循环的规模变小？

有！我现在在调试诶，当然可以修改程序中的数据，直接修改"a"这个数组（注意数组"a"保存在r[3]中），让几百万次的循环规模直接缩小成个位数。

后面具体调试的过程和上面的步骤类似，下面直接给出最终的逻辑。


从列表e中可以得到12个7位数（另其为数组p），恰好与数组"a"中的12个元素一一对应，最终计算：
```python
s=0
for i in range(0,6):
    s+=p[2*i]**a[2*i]+p[2*i+1]**a[2*i+1]
    s%=1125899906842597
```
注：实际计算不是这样，这里为了简化表达

## 快速幂算法
想到快速幂算法应该是不难的，如果参加了第一届比赛的话想到快速幂应该没啥问题。即使不了解这个算法也没关系，稍微搜索一下就能得知。

随手找一个快速幂算法的python实现，直接在函数中调用就可以了。

```py
def fastpower(a,b,n):
    ans = 1
    while n:
        if n&1:
            ans = ans*a%b
        a = a*a%b
        n >>= 1
    return ans%b
```
a是底、n是幂、b是除数

## 虚拟机数值的变换

程序没有像我期待的样子直接运用到200w，而是在101w左右时提示错误的结果。重复上面的流程，好在这次虚拟的逻辑没有变，就是数据变了。

那么问题来了，怎么获取虚拟机的数据呢？

我再一次采用了笨方法：
一次性将数组e按照ascii码的方式转化为字符，然后剔除无法显示的字符，然后根据BigInt将字符串拆分成若干子串，然后通过过滤长度的方法得到保留着数据的子串。子串可能还带有其他字符，需要进一步进行过滤。之后调用int()将子串转化为数字，接着上文的逻辑进行处理。