import './globals.css';

export const metadata = {
  title: 'AI Studio',
  description: 'Creative AI platform',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
