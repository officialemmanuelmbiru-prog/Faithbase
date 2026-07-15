import { Hero } from '@/components/ui/Hero/Hero';

/**
 * Faithbase Homepage — The Invitation
 *
 * This is the first official landing page for Faithbase.
 * It serves as a peaceful, Christ-centered entry point.
 * Future: Will become the loading screen before the 3D Arrival World.
 */
export default function Home() {
  // Placeholder handler - will be connected to navigation later
  const handleBeginJourney = () => {
    // In the future, this will transition to the 3D world
    console.log('🕊️ Begin Your Journey — Navigating to Arrival World');
  };

  const handleLearnMore = () => {
    // In the future, this will navigate to the About page
    console.log('📖 Learn More — Navigating to About');
  };

  return (
    <main>
      <Hero
        onPrimaryClick={handleBeginJourney}
        onSecondaryClick={handleLearnMore}
      />
    </main>
  );
}