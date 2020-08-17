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
