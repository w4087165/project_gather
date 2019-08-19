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
var $form_login=$("$form_login");
var $username=$("#username");
var $password1=$("#password1");
var $password2=$("#password2");
var $err1=$('#err1');
var $err2=$("#err2");
var $err3=$("#err3");
var $err4=$("#err4");
var $btn=$(".btn>input");
// 定义一个验证内容是否为空的验证函数
function checkvalue(){
    if($username.val()!='' &&
        $password1.val()!=''&&
        $password2.val()!=''&&
        $password1.val() == $password2.val())
    {
        return true
    }
    if($username.val().length<6){
        $err1.show()
        log.submit.autohide($err1)
    }

    if($username.val()==''){
        $err1.show()
        log.submit.autohide($err1)
    }
    if($password1.val()==''){
        $err2.show()
        log.submit.autohide($err2)
    }
    if($password2.val()==''){
        $err3.show()
        log.submit.autohide($err3)
    }
    if($password1.val() != $password2.val()){
        $err4.show()
        log.submit.autohide($err4)
    }
    return false
}

function checkvalue2(){
    if($username.val()!='' &&
        $password1.val()!=''&&
    {
        return true
    }
    if($username.val()==''){
        $err1.show()
        log.submit.autohide($err1)
    }
    if($password1.val()==''){
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
$(function(){
    $form_login.on('submit',function(){
       return checkvalue2()
    })
})
