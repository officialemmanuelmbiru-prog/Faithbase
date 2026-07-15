import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'Faithbase — A Digital Sanctuary',
  description:
    'Explore Scripture, experience stories, and grow in Christ through immersive biblical journeys and creative ministry.',
  keywords:
    'faith, Bible, Christian, ministry, church, scripture, journey, creative, digital sanctuary',
  openGraph: {
    title: 'Faithbase — A Digital Sanctuary',
    description:
      'Explore Scripture, experience stories, and grow in Christ through immersive biblical journeys and creative ministry.',
    type: 'website',
    url: 'https://faithbase.app',
    siteName: 'Faithbase',
  },
  viewport: 'width=device-width, initial-scale=1',
  themeColor: '#fef9f0',
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}