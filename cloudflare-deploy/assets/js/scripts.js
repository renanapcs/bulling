// Função para gerar o PDF (simulação)
function generatePDF() {
    // Criar um modal de confirmação mais elegante
    const modal = document.createElement('div');
    modal.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0,0,0,0.8);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 1000;
    `;
    
    const modalContent = document.createElement('div');
    modalContent.style.cssText = `
        background: white;
        padding: 40px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        animation: modalFadeIn 0.3s ease-out;
    `;
    
    modalContent.innerHTML = `
        <h3 style="color: #2c3e50; margin-bottom: 20px;">📄 Cartilha para Impressão</h3>
        <p style="margin-bottom: 15px; color: #666;">A cartilha será aberta em uma nova aba otimizada para impressão.</p>
        <p style="margin-bottom: 30px; color: #666; font-size: 0.9rem;">
            <strong>Instruções:</strong><br>
            • Use <strong>Ctrl+P</strong> para imprimir<br>
            • Escolha <strong>"Salvar como PDF"</strong> como destino<br>
            • Configure para <strong>página A4</strong>
        </p>
        <div style="display: flex; gap: 15px; justify-content: center;">
            <button onclick="confirmDownload()" style="
                background: #2ecc71;
                color: white;
                border: none;
                padding: 12px 25px;
                border-radius: 25px;
                cursor: pointer;
                font-weight: bold;
            ">Abrir Cartilha</button>
            <button onclick="closeModal()" style="
                background: #e74c3c;
                color: white;
                border: none;
                padding: 12px 25px;
                border-radius: 25px;
                cursor: pointer;
                font-weight: bold;
            ">Cancelar</button>
        </div>
    `;
    
    modal.appendChild(modalContent);
    document.body.appendChild(modal);
    
    // Adicionar animação CSS
    const style = document.createElement('style');
    style.textContent = `
        @keyframes modalFadeIn {
            from { opacity: 0; transform: scale(0.8); }
            to { opacity: 1; transform: scale(1); }
        }
    `;
    document.head.appendChild(style);
}

function confirmDownload() {
    // Abrir a cartilha para impressão em nova aba
    const cartilhaWindow = window.open('cartilha-impressao.html', '_blank');
    
    if (cartilhaWindow) {
        // Aguardar o carregamento da página
        cartilhaWindow.onload = function() {
            // Mostrar instruções para o usuário
            showNotification('📄 Cartilha aberta! Use Ctrl+P para imprimir ou salvar como PDF', 'success');
        };
    } else {
        // Fallback se popup for bloqueado
        showNotification('⚠️ Popup bloqueado. Acesse cartilha-impressao.html diretamente', 'warning');
    }
    
    closeModal();
}

function closeModal() {
    const modal = document.querySelector('div[style*="position: fixed"]');
    if (modal) {
        modal.remove();
    }
}

// Função para mostrar notificações
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: ${type === 'success' ? '#2ecc71' : '#3498db'};
        color: white;
        padding: 15px 25px;
        border-radius: 25px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        z-index: 1001;
        animation: slideIn 0.3s ease-out;
        font-weight: bold;
    `;
    
    notification.textContent = message;
    document.body.appendChild(notification);
    
    // Adicionar animação CSS
    const style = document.createElement('style');
    style.textContent = `
        @keyframes slideIn {
            from { transform: translateX(100%); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }
    `;
    document.head.appendChild(style);
    
    // Remover após 3 segundos
    setTimeout(() => {
        notification.style.animation = 'slideIn 0.3s ease-out reverse';
        setTimeout(() => notification.remove(), 300);
    }, 3000);
}

// Adicionar animações adicionais quando a página carrega
document.addEventListener('DOMContentLoaded', function() {
    const pages = document.querySelectorAll('.page');
    
    // Adicionar um atraso progressivo para a animação de cada página
    pages.forEach((page, index) => {
        page.style.animationDelay = `${index * 0.2}s`;
    });
    
    // Adicionar efeito de parallax suave ao scroll
    window.addEventListener('scroll', function() {
        const scrolled = window.pageYOffset;
        const parallax = document.querySelectorAll('.character');
        
        parallax.forEach((element, index) => {
            const speed = 0.5 + (index * 0.1);
            element.style.transform = `translateY(${scrolled * speed}px)`;
        });
    });
    
    // Adicionar efeito de hover nas imagens
    const images = document.querySelectorAll('.illustration');
    images.forEach(img => {
        img.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.05) rotate(2deg)';
        });
        
        img.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1) rotate(0deg)';
        });
    });
    
    // Adicionar contador de visualizações (simulado)
    let viewCount = localStorage.getItem('cartilhaViews') || 0;
    viewCount++;
    localStorage.setItem('cartilhaViews', viewCount);
    
    // Mostrar contador no rodapé
    const footer = document.querySelector('footer p');
    if (footer) {
        footer.innerHTML += `<br><small>👀 Esta cartilha foi visualizada ${viewCount} vezes</small>`;
    }
    
    // Adicionar efeito de digitação no título principal
    const mainTitle = document.querySelector('h1');
    if (mainTitle) {
        const originalText = mainTitle.textContent;
        mainTitle.textContent = '';
        let i = 0;
        
        const typeWriter = () => {
            if (i < originalText.length) {
                mainTitle.textContent += originalText.charAt(i);
                i++;
                setTimeout(typeWriter, 100);
            }
        };
        
        setTimeout(typeWriter, 1000);
    }
    
    // Adicionar botão de voltar ao topo
    const backToTop = document.createElement('button');
    backToTop.innerHTML = '⬆️';
    backToTop.style.cssText = `
        position: fixed;
        bottom: 30px;
        right: 30px;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background: #3498db;
        color: white;
        border: none;
        cursor: pointer;
        font-size: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        z-index: 999;
        opacity: 0;
        transition: all 0.3s ease;
    `;
    
    document.body.appendChild(backToTop);
    
    // Mostrar/esconder botão baseado no scroll
    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 300) {
            backToTop.style.opacity = '1';
        } else {
            backToTop.style.opacity = '0';
        }
    });
    
    // Funcionalidade do botão voltar ao topo
    backToTop.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
    
    // Adicionar efeito de partículas no fundo (opcional)
    createParticles();
});

// Função para criar partículas animadas no fundo
function createParticles() {
    const particleContainer = document.createElement('div');
    particleContainer.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: -1;
    `;
    
    document.body.appendChild(particleContainer);
    
    // Criar partículas
    for (let i = 0; i < 20; i++) {
        const particle = document.createElement('div');
        particle.style.cssText = `
            position: absolute;
            width: 4px;
            height: 4px;
            background: rgba(74, 144, 226, 0.3);
            border-radius: 50%;
            animation: floatParticle ${5 + Math.random() * 10}s infinite linear;
        `;
        
        particle.style.left = Math.random() * 100 + '%';
        particle.style.top = Math.random() * 100 + '%';
        particle.style.animationDelay = Math.random() * 10 + 's';
        
        particleContainer.appendChild(particle);
    }
    
    // Adicionar CSS para animação das partículas
    const style = document.createElement('style');
    style.textContent = `
        @keyframes floatParticle {
            0% { transform: translateY(100vh) rotate(0deg); opacity: 0; }
            10% { opacity: 1; }
            90% { opacity: 1; }
            100% { transform: translateY(-100vh) rotate(360deg); opacity: 0; }
        }
    `;
    document.head.appendChild(style);
}
