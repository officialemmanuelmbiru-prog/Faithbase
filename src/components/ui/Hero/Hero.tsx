import React from 'react';
import { Button } from '../Button/Button';
import styles from './Hero.module.css';

export interface HeroProps {
  title?: string;
  subtitle?: string;
  description?: string;
  primaryButtonText?: string;
  secondaryButtonText?: string;
  onPrimaryClick?: () => void;
  onSecondaryClick?: () => void;
}

export const Hero: React.FC<HeroProps> = ({
  title = 'Faithbase',
  subtitle = 'A Digital Sanctuary for Biblical Journeys and Creative Ministry',
  description = 'Explore Scripture, experience stories, and grow in Christ through immersive journeys designed to strengthen individuals, churches, and ministries.',
  primaryButtonText = 'Begin Your Journey',
  secondaryButtonText = 'Learn More',
  onPrimaryClick,
  onSecondaryClick,
}) => {
  const handlePrimaryClick = () => {
    if (onPrimaryClick) {
      onPrimaryClick();
    } else {
      // Placeholder: This will later navigate to the 3D Arrival World
      console.log('🕊️ Begin Your Journey — Future: Arrival World');
    }
  };

  const handleSecondaryClick = () => {
    if (onSecondaryClick) {
      onSecondaryClick();
    } else {
      // Placeholder: This will later show more info or navigate to about
      console.log('📖 Learn More — Future: About page');
    }
  };

  return (
    <section className={styles.hero} aria-label="Welcome to Faithbase">
      <div className={styles.container}>
        {/* Decorative element - subtle light ray */}
        <div className={styles.lightRay} aria-hidden="true" />

        <div className={styles.content}>
          <h1 className={styles.title}>
            {title}
          </h1>

          <p className={styles.subtitle}>
            {subtitle}
          </p>

          <p className={styles.description}>
            {description}
          </p>

          <div className={styles.actions}>
            <Button
              variant="primary"
              size="large"
              onClick={handlePrimaryClick}
              aria-label="Begin your faith journey"
            >
              {primaryButtonText}
            </Button>

            <Button
              variant="secondary"
              size="large"
              onClick={handleSecondaryClick}
              aria-label="Learn more about Faithbase"
            >
              {secondaryButtonText}
            </Button>
          </div>
        </div>
      </div>
    </section>
  );
};

Hero.displayName = 'Hero';