document.addEventListener("DOMContentLoaded", function() {
    // Function to play the video
    function playVideo() {
        var video = document.getElementById("joinUsVideo");
        video.play();
    }

    // Add click event listener to the "Join Us" button
    var joinUsButton = document.getElementById("joinUsButton");
    joinUsButton.addEventListener("click", playVideo);
});
