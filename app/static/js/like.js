const likeButtons = document.querySelectorAll('.like-btn');
const likeStateColor = {
    like: "#0d6efd",
    unlike: "black"
};

const likeStateContent = {
    like: '<i class="bi bi-hand-thumbs-up-fill"></i>',
    unlike: '<i class="bi bi-hand-thumbs-up"></i>'
};


likeButtons.forEach((btn)=>{

    btn.addEventListener('click', ()=>{
        fetch(`/post/like/${btn.dataset.likeId}`, {
            method: "POST",
        })
        .then(res=>res.json())
        .then(data=>{
            if (data.message === "success"){
                btn.style.color = likeStateColor[data.action];
                btn.innerHTML = likeStateContent[data.action];
            }
            else{
                location.replace(data.redirect_url) 
            }
        })
    })

})

