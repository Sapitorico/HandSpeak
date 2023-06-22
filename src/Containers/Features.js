import React from "react";

export const Features = () => {
    return (
        <>
            <section class="pt-6 pb-7" id="introduccion">
    <div class="container">
        <div class="row">
            <div class="col-md-6 mx-auto text-center">
                <h2 class="heading-black">Introducción</h2>
                <p class="text-muted lead">
                    HandSpeak es una herramienta que permite traducir el lenguaje de signos en tiempo real
                    utilizando inteligencia artificial.
                </p>
                <p class="text-muted lead">
                    Este sistema se ha creado para facilitar y demostrar una de las características más potentes de las
                    redes neuronales convolucionales,
                    facilitar la comunicación entre sordos y oyentes eliminando las barreras lingüísticas existentes.
                </p>
            </div>
        </div>
        <div class="row mt-5" id="detalles">
            <div class="col-md-10 mx-auto">
                <div class="row feature-boxes">
                    <div class="col-md-6 box">
                        <div class="icon-box box-primary">
                            <div class="icon-box-inner">
                                <img src="static/img/hand.png" alt="Descripción de la imagen" width="35" height="35" />
                            </div>
                        </div>
                        <h5>Manos</h5>
                        <p class="text-muted">La forma, orientación, movimiento y ubicación de las manos son algunos de
                            los parámetros clave del lenguaje de signos.</p>
                    </div>
                    <div class="col-md-6 box">
                        <div class="icon-box box-success">
                            <div class="icon-box-inner">
                                <span data-feather="video" width="35" height="35"></span>
                            </div>
                        </div>
                        <h5>Capturar los datos visuales</h5>
                        <p class="text-muted">Captura de imágenes en tiempo real para el proceso de tratamiento de
                            imágenes y clasificación de signos</p>
                    </div>
                    <div class="col-md-6 box">
                        <div class="icon-box box-danger">
                            <div class="icon-box-inner">
                                <span data-feather="cpu" width="35" height="35"></span>
                            </div>
                        </div>
                        <h5>Procesar los datos</h5>
                        <p class="text-muted">
                            Los datos reconocidos visualmente se procesan, Las imágenes representan signos, diferentes
                            partes de la oración</p>
                        <p class="text-muted">
                            visión por ordenador + inteligencia artificial</p>
                    </div>
                    <div class="col-md-6 box">
                        <div class="icon-box box-info">
                            <div class="icon-box-inner">
                                <span data-feather="message-square" width="35" height="35"></span>
                            </div>
                        </div>
                        <h5>Presentar la opción</h5>
                        <p class="text-muted">La frase seleccionada se muestra en la pantalla para que la lea el usuario
                            oyente.</p>
                    </div>
                </div>
            </div>
        </div>
        <div class="row mt-6" id="blog">
            <div class="col-md-6 mr-auto">
                <h2>Beneficios de HandSpeak</h2>
                <p class="mb-5">
                    La principal ventaja de HandSpeak es que permite una
                    comunicación fluida y efectiva entre personas sordas y
                    oyentes, sin necesidad de un intérprete humano.

                    Además, HandSpeak es una herramienta útil en
                    situaciones de emergencia, ya que permite alos
                    servicios de emergencia comunicarse con personas
                    sordas y obtener información importante en tiempo real.</p>

            </div>
        </div>
    </div>
</section>
        </>
    )
}