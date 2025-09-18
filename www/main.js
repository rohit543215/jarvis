$(document).ready(function () {
    // Animation for main prompt
    $('.text').textillate({
        loop: true,
        sync: true,
        in: { effect: 'bounceIn' },
        out: { effect: 'bounceOut' }
    });

    // Unhide SiriWave section
    $('#SiriWave').removeAttr('hidden');

    // Initialize SiriWave animation
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 800,
        height: 200,
        style: "ios9",
        amplitude: 1,
        speed: 0.30,
        autostart: true
    });
    siriWave.start();

    // Animation for Siri message
    $('.siri-message').textillate({
        loop: true,
        sync: true,
        in: { effect: 'fadeInUp', sync: true },
        out: { effect: 'fadeOutUp', sync: true }
    });

    // Mic button click event
    $("#MicBtn").click(function () { 
        console.log("Mic button clicked");
        $("#Oval").attr("hidden", true);
        $("#SiriWave").removeAttr('hidden');
        if (typeof eel !== "undefined") {
            eel.allCommands();
        } else {
            console.warn("Eel is not defined");
        }
    });

    // Keyboard shortcut: Cmd + J to activate assistant
    function doc_keyUp(e) {
        if (e.key === 'j' && e.metaKey) {
            if (typeof eel !== "undefined") {
                eel.playAssistantSound();
                $("#Oval").attr("hidden", true);
                $("#SiriWave").removeAttr("hidden");
                eel.allCommands();
            } else {
                console.warn("Eel is not defined");
            }
        }
    }
    document.addEventListener('keyup', doc_keyUp, false);

    // Assistant play handler
    function playAssistant(message) {
        if (message != "") {
            $("#Oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);
            eel.allCommands(message);
            $("#chatbox").val("");
            $("#MicBtn").attr('hidden', false);
            $('#SendBtn').attr('hidden', true);
        }
    }

    // Input-based button toggle
    function ShowHideButton(message) {
        if (message.length == 0) {
            $('#MicBtn').attr('hidden',false);
            $('#SendBtn').attr('hidden', true);
        } else {
            $('#MicBtn').attr('hidden', true);
            $('#SendBtn').attr('hidden', false);
        }
    }
    $("#chatbox").keyup(function () {

      let message = $("#chatbox").val();
      ShowHideButton(message);
});

$("#SendBtn").click(function () {
    let message = $("#chatbox").val();
    console.log("Sending message:", message);
    playAssistant(message);
});

$("#chatbox").keypress(function (e) {
    key=e.which;
    if(key==13){
        let message = $("#chatbox").val();
        playAssistant(message)
    }
});    

    


   

   

});
