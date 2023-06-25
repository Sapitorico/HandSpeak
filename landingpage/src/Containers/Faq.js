import React from "react";

export const Faq = () => {
    return (
        <section class="py-7" id="PF">
    <div class="container">
        <div class="row">
            <div class="col-md-6 mx-auto text-center">
                <h2>Preguntas frecuentes</h2>
            </div>
        </div>
        <div class="row mt-5">
            <div class="col-md-10 mx-auto">
                <div class="row">
                    <div class="col-md-6 mb-5">
                        <h6>Cómo funciona HandSpeak?</h6>
                        <p class="text-muted">

                            HandSpeak utiliza una combinación de tecnologías de
                            reconocimiento de imágenes y gestos para identificar
                            los movimientos de las manos y dedos de la persona
                            que está hablando en lenguaje de señas.

                            Estos movimientos se convierten en texto escrito
                            utilizando algoritmos de procesamiento de lenguaje
                            natural.
                        </p>
                    </div>
                    <div class="col-md-6 mb-5">
                        <h6>Que desafíos enfrenta?</h6>
                        <p class="text-muted">
                            HandSpeak todavía enfrenta
                            algunos desafíos técnicos, como la variabilidad de las imagenes,
                            iluminacion, fondos, entornos complejos.
                        </p>
                    </div>
                    <div class="col-md-6 mb-5">
                        <h6>Futuro de HandSpeak</h6>
                        <p class="text-muted">
                            A medida que se mejore la red neuronal, se espera que HandSpeak mejore su precisión y
                            A medida que se mejore la red neuronal, se espera que HandSpeak mejore su precisión y
                            gestos y señales.</p>
                        <p class="text-muted">
                            Además de extenderse a varias plataformas de videoconferencia como google met
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
    )
}