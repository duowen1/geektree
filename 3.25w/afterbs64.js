var para=['A5473788'];
(function(a,b){
    var fun1=function(t){
        while(--t){
            a['push'](a['shift']());
        }
    };
    fun1(++b);
}(para,0x196));

var fun=function(a,_0xe936d8){
    a=a-0x0;
    var res=para[a];
    return res;
};

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