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

//var idHouse = 0;

function addMessage(idHouse, message){
    console.log("Evento para adicionar mensagem");
    m = new Paho.MQTT.Message(message);
    m.destinationName = 'm';
    client.send(m);
    Materialize.toast('Mensagem publicada no ambiente', 24000);
    //$('.loadadd').removeClass("semfunc");
    
    $.ajax({
        url : "/house/add/message/",
        type : "POST",
        data : { 
            house : idHouse,
            message : message,
            is_m : '1'
             },



        success : function(json) {
            console.log("Resultado do processamento: "+json);
            if (json == true) {
                Materialize.toast('Mensagem salva no banco de dados', 24000);
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
}

$('#f').submit(function() {
    var form = $(this);
    $.post(form.attr('action'), form.serialize(), function(retorno) {
        if ($("#pesquisa").val() !== "") {
        var searchValue = $("#pesquisa").val();
          console.log($("#pesquisa").val());
          //window.location.replace("/search="+ $("#pesquisa").val() +"");
        }
    });
    return false;
});

function search_users(idHouse, message){
    console.log("Evento para adicionar mensagem");
    //$('.loadadd').removeClass("semfunc");
    
    $.ajax({
        url : "/house/search_users/",
        type : "POST",
        data : { 
            house : idHouse,
            message : message
             },
        success : function(json) {
            $('.resultData').html("");
            $('.resultTxt').html("");
            
            if (json != false) {

                console.log("Resultado do processamento: "+json);
                  $('.resultTxt').html(
                '<h6>Resultados para <i>'+ message +'</i>:<h6>');
                for (var i = json.length - 1; i >= 0; i--) {
                    $('.resultData').append("<li class='collection-item'><div><a href='#'><b>"+ json[i].username +"</b><span style='color: black;''> (" + json[i].email +")</span></a><a id='idsuserlink"+json[i].pk+"' href='#' onclick='add_user("+json[i].pk+", "+idHouse+")' class='secondary-content'><i class='material-icons idsuser"+json[i].pk+"'>person_add</i></a></div></li>");
                    console.log(json[i].username);
                }
                //parent.window.document.location.href = '';
            } else {
                Materialize.toast('Nenhum resultado', 4000);
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

function add_user(idUser, idHouse) {
    $.ajax({
        url : "/house/add_user/",
        type : "POST",
        data : { 
            house : idHouse,
            iduser : idUser
             },
        success : function(json) {
            if (json != false) {
                $('.idsuser'+idUser).html("clear");
                $('#idsuserlink'+idUser).attr("onclick", "remove_user("+idUser+","+idHouse+")")
                console.log("Resultado do processamento: "+json);
                Materialize.toast('Membro adicionado!', 4000);
                $('.warn').html("<p>*Algumas mudanças foram feitas. Recarregue a página para ver a lista atualizada.</p><a class='waves-effect waves-light btn' href=''><i class='material-icons right'>loop</i>Atualizar lista</a>");
                 
                //parent.window.document.location.href = '';
            } else {
                Materialize.toast('Nenhum resultado', 4000);
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

function add_actuator(name, topic, desc, idactuator, idhouse) {
    $.ajax({
        url : "/house/add_actuator/",
        type : "POST",
        data : { 
            name : name,
            topic : topic,
            desc : desc,
            idactuator : idactuator,
            idhouse : idhouse
             },
        success : function(json) {
            if (json != false) {
                console.log("Resultado do processamento: "+json);
                Materialize.toast('Atuador/sensor salvo!', 4000);
                $('.warn').html("<p>*Algumas mudanças foram feitas. Recarregue a página para ver a lista atualizada.</p><a class='waves-effect waves-light btn' href=''><i class='material-icons right'>loop</i>Atualizar lista</a>");
                 
                //parent.window.document.location.href = '';
            } else {
                Materialize.toast('Erro! Verifique se todos os campos foram completados.', 4000);
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

function remove_actuator(idActuator, idHouse) {
    console.log(idActuator);
    console.log(idHouse);
    $.ajax({
        url : "/house/remove_actuator/",
        type : "POST",
        data : { 
            actuator : idActuator,
            house : idHouse
             },
        success : function(json) {
            if (json != false) {
                $('#idsactuator'+idActuator).css("text-decoration", "line-through");
                $('#idsactuatorlink'+idActuator).html("");
                console.log("Resultado do processamento: "+json);
                Materialize.toast('Atuador/sensor removido!', 4000);
                $('.warn').html("<p>*Algumas mudanças foram feitas. Recarregue a página para ver a lista atualizada.</p><a class='waves-effect waves-light btn' href=''><i class='material-icons right'>loop</i>Atualizar lista</a>");
                 
                //parent.window.document.location.href = '';
            } else {
                Materialize.toast('Nenhum resultado', 4000);
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

function remove_user(idUser, idHouse) {
    $.ajax({
        url : "/house/remove_user/",
        type : "POST",
        data : { 
            house : idHouse,
            iduser : idUser
             },
        success : function(json) {
            if (json != false) {
                $('.idsuser'+idUser).html("person_add");
                $('#idsuserlink'+idUser).attr("onclick", "add_user("+idUser+","+idHouse+")")
                console.log("Resultado do processamento: "+json);
                Materialize.toast('Membro removido!', 4000);
                $('.warn').html("<p>*Algumas mudanças foram feitas. Recarregue a página para ver a lista atualizada.</p><a class='waves-effect waves-light btn' href=''><i class='material-icons right'>loop</i>Atualizar lista</a>");
                 
                //parent.window.document.location.href = '';
            } else {
                Materialize.toast('Nenhum resultado', 4000);
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

function addTopic(idHouse, topic, message) {
    m = new Paho.MQTT.Message(message);
    m.destinationName = topic;
    client.send(m);
    Materialize.toast('Mensagem publicada no ambiente', 24000);
    addAction(idHouse, 'publicou o tópico <b>'+ topic +'</b> com a mensagem <b> '+message+' </b>');
}

function addAction(idHouse, message){

    //$('.loadadd').removeClass("semfunc");
    
    $.ajax({
        url : "/house/add/message/",
        type : "POST",
        data : { 
            house : idHouse,
            message : message,
            is_m : '0'
             },



        success : function(json) {
            console.log("Resultado do processamento: "+json);
            if (json == true) {
                Materialize.toast('Mensagem salva no banco de dados', 24000);
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
}

function alterCheck(nameAc, numAc, topicAc) {
    console.log(nameAc);
    console.log($('#element'+numAc).prop('checked'));

    bool = $('#element'+numAc).prop('checked');

    if(bool == true){
        m = new Paho.MQTT.Message('on');
    }else{
        m = new Paho.MQTT.Message('off');
    }

    console.log(m);
    m.destinationName = topicAc;
    client.send(m);
    Materialize.toast('Mensagem publicada no ambiente. Aguarde a confirmação...', 24000);
    $('#element'+numAc).prop('disabled', 'true');
    if(bool == true){
        addAction(idHouse, 'ligou o atuador <b>"'+ nameAc + '"</b>');
    }else{
        addAction(idHouse, 'desligou o atuador <b>"'+ nameAc + '"</b>');
    }

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


var id = 6;