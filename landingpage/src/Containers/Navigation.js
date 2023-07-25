import React from "react";

const Navigation = () => {
    return (
        <>
<section class="smart-scroll">
    <div class="container-fluid">
        <nav class="navbar navbar-expand-md navbar-dark">
            <a class="navbar-brand heading-black" href="../templates/index.html">
                HandSpeak
            </a>
            <button class="navbar-toggler navbar-toggler-right border-0" type="button" data-toggle="collapse"
                    data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false"
                    aria-label="Toggle navigation">
                <span data-feather="grid"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarCollapse">
                <ul class="navbar-nav ml-auto">
                    <li class="nav-item">
                        <a class="nav-link page-scroll" href="#introduccion">Introducción</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link page-scroll" href="#detalles">Detalles</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link page-scroll" href="#PF">PF</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link page-scroll d-flex flex-row align-items-center text-primary" href="">
                            <em data-feather="layout" width="18" height="18" class="mr-2"></em>
                            HandSpeak
                        </a>
                    </li>
                </ul>
            </div>
        </nav>
    </div>
</section>
    </>
    )
} 

export default Navigation;