Materialize.toast('Conectando ao broker do ambiente ' + adata["name"], 24000);

// Create a client instance
client = new Paho.MQTT.Client(adata.server, parseInt(adata.portws),adata.key); 
//Example client = new Paho.MQTT.Client("m11.cloudmqtt.com", 32903, "web_" + parseInt(Math.random() * 100, 10));

// set callback handlers
client.onConnectionLost = onConnectionLost;
client.onMessageArrived = onMessageArrived;
var options = {
	useSSL: true,
	userName: adata.user,
	password: adata.password,
	onSuccess:onConnect,
	onFailure:doFail
}

// connect the client
client.connect(options);

// called when the client connects
function onConnect() {
	// Once a connection has been made, make a subscription and send a message.
	Materialize.toast('Conexão estabelecida para o ambiente ' + adata["name"], 24000);
	console.log("onConnect");
	$('#connectInfo').html("conectado");
	for (var i = jdata.length - 1; i >= 0; i--) {
		client.subscribe("r/"+jdata[i].topic);

	}

	client.subscribe("m");
	message1 = new Paho.MQTT.Message("state");
	message1.destinationName = "luz1";
	message2 = new Paho.MQTT.Message("state");
	message2.destinationName = "luz2";

	client.send(message1);
	client.send(message2); 
}

function doFail(e){
	Materialize.toast('Erro ao conectar: ' + e, 24000);
console.log(e);
}

// called when the client loses its connection
function onConnectionLost(responseObject) {
if (responseObject.errorCode !== 0) {
	//Materialize.toast('Conexão perdida: ' + responseObject.errorMessage, 24000);
  console.log("onConnectionLost:"+responseObject.errorMessage);
}
}

// called when a message arrives
function onMessageArrived(message) {
	$('.reloadtl').html("<a class='waves-effect waves-light btn green tooltipped' data-position='top' data-delay='50' data-tooltip='*Apenas mensagens originadas da plataforma CASINHA são salvas no banco' href=''><i class='material-icons right'>refresh</i>*Atualize a lista</a>");
	for (var i = jdata.length - 1; i >= 0; i--) {
		console.log(message.destinationName + " == " + "r/"+jdata[i].topic + "?");
		if (message.destinationName == "r/"+jdata[i].topic) {
			//console.log("sim");
			$("#element"+jdata[i].value).prop('disabled', null);
			if (jdata[i].type == "1" || jdata[i].type == "4") {
				if (message.payloadString == "on") {
					$("#element"+jdata[i].value).prop('checked', true);
					$("#icon"+jdata[i].value).addClass('yellow');
					Materialize.toast('Mensagem no ambiente ' + jdata[i].name + ' foi ligado(a) neste momento', 24000);
					//addAction(idHouse, 'ligou o atuador <b>'+ jdata[i].name);
				} else {
					$("#element"+jdata[i].value).prop('checked', null);
					$("#icon"+jdata[i].value).removeClass('yellow')
					Materialize.toast('Mensagem no ambiente ' + jdata[i].name + ' foi desligado(a) neste momento', 24000);
					//addAction(idHouse, 'desligou o atuador <b>'+ jdata[i].name);
				}
				
			} else{
				$("#element"+jdata[i].value).html(message.payloadString);
			}
		}
	}
	if(message.destinationName == "r/luz1"){
		$("#luz1").html(message.payloadString);
	}else if(message.destinationName == "r/luz2"){
		$("#luz2").html(message.payloadString);
	}else{
		Materialize.toast('Mensagem no ambiente ' + adata.name + ': '+message.payloadString, 24000);
	}
	//console.log("onMessageArrived:"+message.payloadString);
console.log("onMessageArrived:"+message.destinationName);
}