var $messages = $(".messages-content"),
  d,
  h,
  m,
  speech
i = 0

$(window).load(function () {
  $messages.mCustomScrollbar()
  setTimeout(function () {
    insertResponseMessage("hello i am bilal bot")
  }, 100)
  speech = speechSynthesis
})

function updateScrollbar() {
  $messages.mCustomScrollbar("update").mCustomScrollbar("scrollTo", "bottom", {
    scrollInertia: 10,
    timeout: 0
  })
}

function setDate() {
  d = new Date()
  if (m != d.getMinutes()) {
    m = d.getMinutes()
    $('<div class="timestamp">' + d.getHours() + ":" + m + "</div>").appendTo(
      $(".message:last")
    )
  }
}

function insertPersonalMessage(message) {
  $('<div class="message message-personal">' + message + "</div>")
    .appendTo($(".mCSB_container"))
    .addClass("new")
  updateScrollbar()
}

function insertLoadingMessage() {
  $(
    '<div class="message loading new"><figure class="avatar"><img src="../static/img/bat.png"/></figure><span></span></div>'
  ).appendTo($(".mCSB_container"))
  updateScrollbar()
}

function insertResponseMessage(response) {
  $(".message.loading").remove()
  $(
    '<div class="message new"><figure class="avatar"><img src="../static/img/bat.png"/></figure>' +
      response +
      "</div>"
  )
    .appendTo($(".mCSB_container"))
    .addClass("new")
  setDate()
  updateScrollbar()
}

function insertAudioMessage(audioUrl) {
  audioElement =
    '<audio controls autoplay><source src="' +
    audioUrl +
    '" type="audio/mp3"></audio>'
  $(
    '<div class="message new"><figure class="avatar"><img src="../static/img/bat.png"/></figure>' +
      audioElement +
      "</div>"
  )
    .appendTo($(".mCSB_container"))
    .addClass("new")
  setDate()
  updateScrollbar()
}

function insertKeyboardMessage() {
  message = $(".message-input").val()
  if ($.trim(message) == "") {
    return false
  }
  insertPersonalMessage(message)
  insertLoadingMessage()
  sendToServer(message)
}
