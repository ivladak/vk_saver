var regex = /3pm\.[^":]+\/\/:s?ptth/g; // The 'g' modifier for advancing the pointer.

String.prototype.reverse = function() {
    return this.split("").reverse().join("");
}

var full_text = document.body.innerHTML;
var text_reversed = full_text.reverse()

var match;
do {
  match = regex.exec(text_reversed);
  if (match)
    console.log(match[0].reverse());
} while (match);
