export default function HomePage() {
  return (
    <main style={{ padding: 32, fontFamily: 'Arial, sans-serif', background: '#0f172a', minHeight: '100vh', color: '#e2e8f0' }}>
      <h1>AI Studio</h1>
      <p>Creative AI workspace for chat, images and video.</p>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: 18, marginTop: 24 }}>
        <Card title="Chat" description="Conversation and persona-aware AI" />
        <Card title="Image" description="Text-to-image generation" />
        <Card title="Video" description="Text-to-video and motion" />
        <Card title="Persona" description="User identity and style settings" />
      </div>
    </main>
  );
}

function Card({ title, description }: { title: string; description: string }) {
  return (
    <div style={{ border: '1px solid #334155', borderRadius: 12, padding: 20, background: '#111827' }}>
      <h3>{title}</h3>
      <p>{description}</p>
    </div>
  );
}
