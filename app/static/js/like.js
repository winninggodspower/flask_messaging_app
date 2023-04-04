const likeButtons = document.querySelectorAll('.like-btn');
const likeStateColor = {
    like: "#0d6efd",
    unlike: "black"
};

const likeStateContent = {
    like: '<i class="bi bi-hand-thumbs-up-fill"></i>',
    unlike: '<i class="bi bi-hand-thumbs-up"></i>'
};

const likeStateCount = {
    like: +1,
    unlike: -1
};

document.querySelectorAll('.loading-gif').forEach(gif=>{
    gif.style.display = "none";
})

likeButtons.forEach((btn)=>{

    btn.addEventListener('click', ()=>{
        let postId = btn.dataset.likeId
        let loadingGif = document.getElementById(postId+'-loading-gif');
        loadingGif.style.display = "inline";

        fetch(`/post/like/${postId}`, {
            method: "POST",
        })
        .then(res=>res.json())
        .then(data=>{
            if (data.message === "success"){
                btn.style.color = likeStateColor[data.action];
                btn.innerHTML = likeStateContent[data.action];
                
                // change like count
                let likeCount = document.getElementById(`${postId}-like-count`)
                let newLikeCount = parseInt(likeCount.innerText) + likeStateCount[data.action];
                likeCount.innerText = newLikeCount;
            }
            else{
                location.replace(data.redirect_url) 
            }
            loadingGif.style.display = "none"
        })

    })

})

