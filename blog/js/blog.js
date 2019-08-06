//针对log页定义一个对象
var log={
    startdt:"2019-8-5",
    enddt:"2019-9-5",
    updatedt:'2019-8-8',
    anchor:'ysfu',
}
//由对象派生业务逻辑
log.submit={
    autohide:function(jq){
        setTimeout(function(){
            jq.hide()
        },2000)
    }
}
//获取元素对象，并绑定到变量中
var $form=$("form");
var $username=$("#username");
var $password=$("#password");
var $err1=$('#err1');
var $err2=$("#err2")
var $btn=$(".btn>input")
// 定义一个验证内容是否为空的验证函数
function checkvalue(){
    if($username.val()!='' && $password.val()!=''){
        return true
    }
    if($username.val()==''){
        $err1.show()
        log.submit.autohide($err1)
    }
    if($password.val()==''){
        $err2.show()
        log.submit.autohide($err2)
    }
    return false   
}
//绑定按钮的单机事件
$(function(){
    $form.on('submit',function(){
       return checkvalue()
    })
})
//定义一个给予列表页的业务逻辑
var lst={
    template:function(title,imgs,p,p2){
        var html = ''
        
        html +='<div class="item">'
        html +='<div class="title">'
        html +='<h3>'+title+'</h3>'
        html +='</div>'
        html +='<div class="con">'
        html +='<div class="cleft">'
        html +='<img src="'+imgs+'" alt="">'
        html +='</div>'
        html +='<div class="cright">'
        html +='        <p class="ptop">'
        html +=             p
        html +='        </p>'
        html +='        <p class="pbottom">'
        html +=             p2
        html +='        </p>'
        html +='    </div>'
        html +='</div>'
        html +='</div>'
        return html;
        
    }
}
// 追加数据
$(".lit").append(lst.template('Python语言','imgs/b.jpg','今天是个好日子，明天回事大庆其他那，后天优势一个好天气，天天都有好新奇','pipjd152566 56465 99996'))

// 定义一个我的图片页的业务对象
var myipics = {
    template:function(pic,number,title){
        var html = ''
        html+='<div class="item">'
        html+='<div class="imgs">'
        html+='    <img src="'+pic+'" alt="">'
        html+='    <div class="tip">喜欢|'+number+'</div>'
        html+='</div>'
        html+='<div class="title">'
        html+='    <h3>'+title+'</h3>'
        html+='</div>'
        html+='</div>'
        return html
    }
}
// 追加数据
var picslist=[{u:'imgs/toppic02.jpg',n:998,p:'滴滴滴哒哒哒'},
              {u:'imgs/banner01.jpg',n:887,p:'流动的墙'},
              {u:'imgs/banner02.jpg',n:1507,p:'AI时代实录'},
              {u:'imgs/banner03.jpg',n:556,p:'锅里各嘎'},
              {u:'imgs/zd01.jpg',n:885,p:'锅里各嘎'}]
for(var i=0;i<picslist.length;i++){
    $('#pics').append(myipics.template(picslist[i].u,picslist[i].n,picslist[i].p))
}