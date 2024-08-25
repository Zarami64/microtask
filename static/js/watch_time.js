var watchTime = 0;
var interval = setInterval(function() {
    watchTime += 1;
    document.getElementById('watch-time').innerText = 'Watch Time: ' + watchTime + ' seconds';
}, 1000);

document.querySelector('iframe').onload = function() {
    clearInterval(interval);
};
