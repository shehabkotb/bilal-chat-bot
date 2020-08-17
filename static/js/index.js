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
