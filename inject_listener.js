const fs = require('fs');
const glob = require('glob');

const script = `
<script>
window.addEventListener('message', (e) => {
  if (e.data && e.data.type === 'UPDATE_THEME' && e.data.colors && e.data.colors.length > 0) {
    const primary = e.data.colors[0];
    const root = document.documentElement;
    
    let styleTag = document.getElementById('dynamic-theme-override');
    if (!styleTag) {
      styleTag = document.createElement('style');
      styleTag.id = 'dynamic-theme-override';
      document.head.appendChild(styleTag);
    }
    
    styleTag.innerHTML = \`
      :root {
        --primary: \${primary} !important;
        --accent: \${primary} !important;
        --button-bg: \${primary} !important;
        --apple-blue: \${primary} !important;
        --link-blue: \${primary} !important;
        --blue: \${primary} !important;
        --brand: \${primary} !important;
      }
      .bg-primary, .bg-accent, .bg-blue-600 { background-color: \${primary} !important; }
      .text-primary, .text-accent { color: \${primary} !important; }
      button { background-color: \${primary} !important; border-color: \${primary} !important; }
      a { color: \${primary} !important; }
    \`;
  }
});
</script>
`;

glob.sync('design-md/**/*.html').forEach(file => {
  let content = fs.readFileSync(file, 'utf8');
  if (!content.includes('UPDATE_THEME')) {
    content = content.replace('</body>', `${script}\n</body>`);
    fs.writeFileSync(file, content);
  }
});