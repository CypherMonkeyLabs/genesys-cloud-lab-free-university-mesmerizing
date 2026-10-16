/* Adapted from the Webex lab footer helper.
   The Genesys footer is already in the page. This marks it so the kit CSS applies.
   It does not inject other labs or social networks. */
(function () {
  var foot = document.querySelector(".site-footer");
  if (!foot) return;
  foot.classList.add("lab-footer");
  foot.setAttribute("data-canon-footer", "");
})();
