/* Adapted from the Webex lab frame. Genesys keeps its own drawer and banner.
   This file only scrolls that one-row banner. It does not add social links. */
(function () {
  var rail = document.getElementById("section-rail");
  function nudge(dx) {
    if (!rail) return;
    var reduce = document.documentElement.dataset.reduce === "1";
    rail.scrollBy({ left: dx, behavior: reduce ? "auto" : "smooth" });
  }
  var prev = document.getElementById("rail-prev");
  var next = document.getElementById("rail-next");
  if (prev) prev.addEventListener("click", function () { nudge(-240); });
  if (next) next.addEventListener("click", function () { nudge(240); });
})();
