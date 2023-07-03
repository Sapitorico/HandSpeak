import React, { Component } from 'react';
import {
  Carousel,
  CarouselItem,
  CarouselControl,
  CarouselIndicators,
  CarouselCaption
} from 'reactstrap';
import 'bootstrap';

/* impot images */
import ScrenEducation from '../static/img/Screenshot-educations.png'
import ScrenInicio from '../static/img/Screenshot-inicio.png'
import ScrenPractice from '../static/img/Screenshot-practice.png'
import ScrenSetting from '../static/img/Screenshot-settings.png'

const items = [
  {
    src: ScrenInicio,
    altText: 'screnshot of inicio windows',
    caption: ''
  },
  {
    src: ScrenEducation,
    altText: 'screnshot of Education windows',
    caption: ''
  },
  {
    src: ScrenPractice,
    altText: 'screnshot of practice windows',
    caption: ''
  },
  {
    src: ScrenSetting,
    altText: 'screnshot of setting windows',
    caption: ''
  }
];

class Examples extends Component {
  constructor(props) {
    super(props);
    this.state = { activeIndex: 0 };
    this.next = this.next.bind(this);
    this.previous = this.previous.bind(this);
    this.goToIndex = this.goToIndex.bind(this);
    this.onExiting = this.onExiting.bind(this);
    this.onExited = this.onExited.bind(this);
  }

  onExiting() {
    this.animating = true;
  }

  onExited() {
    this.animating = false;
  }

  next() {
    if (this.animating) return;
    const nextIndex = this.state.activeIndex === items.length - 1 ? 0 : this.state.activeIndex + 1;
    this.setState({ activeIndex: nextIndex });
  }

  previous() {
    if (this.animating) return;
    const nextIndex = this.state.activeIndex === 0 ? items.length - 1 : this.state.activeIndex - 1;
    this.setState({ activeIndex: nextIndex });
  }

  goToIndex(newIndex) {
    if (this.animating) return;
    this.setState({ activeIndex: newIndex });
  }

  render() {
    const { activeIndex } = this.state;

    const slides = items.map((item) => {
      return (
        <CarouselItem
          onExiting={this.onExiting}
          onExited={this.onExited}
          key={item.src}
        >
          <img src={item.src} alt={item.altText} width="600px" />
          <CarouselCaption captionText={item.caption} captionHeader={item.caption} />
        </CarouselItem>
      );
    });

    return (
      <div class="pt-6 pb-7" id="introduccion">
        <div class="container">
          <div class="row">
            <div class="col-md-6 mx-auto text-center">
              <Carousel
                activeIndex={activeIndex}
                next={this.next}
                previous={this.previous}
              >

                <CarouselIndicators items={items} activeIndex={activeIndex} onClickHandler={this.goToIndex} />
                {slides}
                <CarouselControl direction="prev" directionText="Previous" onClickHandler={this.previous} />
                <CarouselControl direction="next" directionText="Next" onClickHandler={this.next} />
              </Carousel>
            </div>
          </div>
        </div>
      </div>
    );
  }
}


export default Examples;