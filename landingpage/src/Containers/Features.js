import React from "react";

import hand from "../static/icons/icon-hand-w.png";
import data from "../static/icons/icon-data-w.png";
import display from "../static/icons/icon-display-w.png";
import video from "../static/icons/icon-video-w.png";

export const Features = () => {
    return (
        <>
            <section class="pt-6 pb-7" id="introduccion">
    <div class="container">
        <div class="row">
            <div class="col-md-6 mx-auto text-center">
                <h2 class="heading-black">Introducción</h2>
                <p class="text-muted lead">
                    HandSpeak es una herramienta que permite interpretar la lengua de señas en tiempo real
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
                                <img src={hand} alt="imagen" width="35" height="35" />
                            </div>
                        </div>
                        <h5>Manos</h5>
                        <p class="text-muted">La forma, orientación, movimiento y ubicación de las manos son algunos de
                            los parámetros clave de la lengua de señas.</p>
                    </div>
                    <div class="col-md-6 box">
                        <div class="icon-box box-success">
                            <div class="icon-box-inner">
                            <img src={video} alt="imagen" width="35" height="35" />
                            </div>
                        </div>
                        <h5>Capturar los datos visuales</h5>
                        <p class="text-muted">Captura de imágenes en tiempo real para el proceso de tratamiento de
                            imágenes y clasificación de signos</p>
                    </div>
                    <div class="col-md-6 box">
                        <div class="icon-box box-info">
                            <div class="icon-box-inner">
                            <img src={data} alt="imagen" width="35" height="35" />
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
                            <img src={display} alt="imagen" width="35" height="35" />
                            </div>
                        </div>
                        <h5>Presentar la opción</h5>
                        <p class="text-muted">La frase seleccionada se muestra en la pantalla para que la lea el usuario
                            oyente.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
        </>
    )
}