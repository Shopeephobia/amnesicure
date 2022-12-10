function showQuestion(idx){
    $('#question').text(data.questions[idx]);
}

function correctFeedback(){
    $('.feedback_container').append('<div class="alert alert-success" role="alert"> Correct </div>');
}

function wrongFeedback(idx){
    $('.feedback_container').append('<div class="alert alert-danger" role="alert"> Wrong: The answer is "'+data.answers[idx]+'"</div>');
}

function clearFeedback(){
    $('.feedback_container').empty();
}

function submitResult(pk, isCorrect){
    $.ajax({
        type: "POST",
        url: window.location.href,
        data: {
            id: pk,
            answer: isCorrect
        }
      });
}

$(document).ready(function(){
    $("#next").toggle();
    let idx = 0;
    showQuestion(idx);

    $("#submit").click(function(){
        var answer = $("#answer").val();
        var isCorrect = 0;
        if (answer === data.answers[idx]){
            correctFeedback();
            isCorrect = 1;
        }
        else{
            wrongFeedback(idx);
        }
        submitResult(data.ids[idx]);
        $("#submit").toggle();
        $("#next").toggle();
    })

    $("#next").click(function(){
        idx = idx+1;
        if (idx == length){
            window.location.replace(window.location.origin + "/review");
        }
        clearFeedback();
        showQuestion(idx);
        $("#answer").val("");
        $("#next").toggle();
        $("#submit").toggle();
    })
})