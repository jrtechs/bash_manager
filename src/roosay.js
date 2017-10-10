#!/usr/bin/env node
(function () {
    var DEFAULT_LEN, ROO, BUBBLE_TOP_CHAR,
        textToRoo;

    DEFAULT_LEN = 35;
    BUBBLE_TOP_CHAR = "-";

    roo = `
           \\    /)/)
            \\  (ø.ø)
                \\ (    />
              __/ _\\  //
             '~( '~ )//
               _\\  '}/
              \\"--~(/`;

    function lineify(maxLen) {
        function bar([word, ...words], [line, ...lines]) {
            if (!word) return [pad(line), ...lines];
            word = word.trim();
            if (!line) return bar(words, [word, ...lines]);
            return bar(words, (word.length + line.length < maxLen)
                ? [[line, word].join(" "), ...lines]
                : [word, pad(line), ...lines]);
        }
        function pad(line) {
            return line + new Array(maxLen - line.length).fill(" ").join("");
        }
        return (s => bar(s.split(" "), [""]).reverse());
    }

    function rooify(text) {
        var textLines, finalOutput, bubbleHeader;
        finalOutput = "";
        textLines = lineify(DEFAULT_LEN)(text);
        bubbleHeader = new Array(DEFAULT_LEN+2).fill(BUBBLE_TOP_CHAR).join("");
        finalOutput += "/" + bubbleHeader + "\\\n";
        textLines.forEach(l => finalOutput += "| " + l + " |\n");
        finalOutput += "\\" + bubbleHeader + "/";
        finalOutput += roo;
        return finalOutput;
    }

    if (process.stdin.isTTY) {
        textToRoo = process.argv.splice(2).join(" ");
        console.log(rooify(textToRoo));
    } else {
        textToRoo = "";
        process.stdin.on('data', b => textToRoo += b.toString());
        process.stdin.on('end', _ => console.log(rooify(textToRoo)));
        process.stdin.resume();
    }
}());