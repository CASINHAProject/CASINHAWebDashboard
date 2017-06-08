$('#sign').submit(function() {
    var form = $(this);
    $('.t1').addClass("semfunc");
    $.post(form.attr('action'), form.serialize(), function(retorno) {
        
        var iName = $('#aunome').val()
        var iPass = $('#ausenha').val()
        if (iName == '' || iPass == '') {
            $('.t1').removeClass("semfunc");
        } else{
            $('.pre1').removeClass("semfunc");
            $.ajax({
                url : "/autentica/",
                type : "POST",
                data : { 
                    username : iName,
                    password : iPass,
                     },

                success : function(json) {
                    if (json == true) {
                        parent.window.document.location.href = '/';
                    } else {
                        $('.pre1').addClass("semfunc");
                        $('.t1').removeClass("semfunc");
                        
                    }            
                },

                error : function(xhr,errmsg,err) {
                    console.log(xhr.status + ": " + xhr.responseText);
                   $('.pre1').addClass("semfunc");
                   $('.t1').removeClass("semfunc");

                }
            }); 
        }
    });
    return false;
});

$('#register').submit(function() {
    var form = $(this);
    $('.t1').addClass("semfunc");
    $.post(form.attr('action'), form.serialize(), function(retorno) {
        
        var iName = $('#nomer').val();
        var iEmail = $('#emailr').val();
        var iSenha = $('#passwordr').val();

        if (iName == '' || iEmail == '' || iSenha == '') {
            $('.t2').removeClass("semfunc");
        } else{
            $('.pre2').removeClass("semfunc");
            $.ajax({
                url : "/registra/",
                type : "POST",
                data : { 
                    username : iName,
                    email : iEmail,
                    password : iSenha,
                     },

                success : function(json) {
                    console.log("Resultado do processamento: "+json);
                    if (json == true) {
                        parent.window.document.location.href = '/';
                    } else {
                        $('.pre2').addClass("semfunc");
                        $('.t2').removeClass("semfunc");
                        
                    }            
                },

                error : function(xhr,errmsg,err) {
                    console.log(xhr.status + ": " + xhr.responseText);
                   $('.pre2').addClass("semfunc");
                   $('.t2').removeClass("semfunc");

                }
            }); 
        }
    });
    return false;
});

function delete_account(){
    $.ajax({
        url : "/deletaconta/",
        type : "GET",
        
        success : function(json) {
            if (json == true) {
                parent.window.document.location.href = '';
            } else {
                alert("Something went wrong....");
            }            
        },

        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText);
           alert("Something went wrong.")

        }
    }); 
       
}

function addHouse(){
    console.log("apertado");
    var name = $("#name").val();
    var server = $("#server").val();
    var user = $("#user").val();
    var password = $("#password").val();
    var port = $("#port").val();
    //$('.loadadd').removeClass("semfunc");
    $.ajax({
        url : "/house/add/",
        type : "POST",
        data : { 
            name : name,
            server : server,
            user : user,
            password : password,
            portws : port
             },



        success : function(json) {
            console.log("Resultado do processamento: "+json);
            if (json == true) {
                parent.window.document.location.href = '/';
            } else {
                Materialize.toast('Complete todos os campos', 4000);
                //$('.loadadd').addClass("semfunc");
            }            
        },

        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText);
           Materialize.toast('Erro: '+xhr.status, 4000);
           //$('.loadadd').addClass("semfunc");

        }
    }); 
        

    return false;
    
}

//Cookies globais padrões para utilização do AJAX

function getCookie(name) {
        var cookieValue = null;
        var i = 0;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (i; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        crossDomain: false, // obviates need for sameOrigin test
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });


