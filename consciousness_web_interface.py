"""
Consciousness Web Interface
Web-based interface for the Qi² Trinity Blockchain

This creates a simple web interface for interacting with the consciousness ledger.
"""

import json
import time
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from qi2_trinity_blockchain import *
from consciousness_economics import *

class ConsciousnessWebHandler(BaseHTTPRequestHandler):
    """HTTP handler for consciousness blockchain web interface"""
    
    # Class variables to store blockchain state
    blockchain = None
    economics = None
    market = None
    user_interfaces = {}
    
    def do_GET(self):
        """Handle GET requests"""
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        
        if path == '/':
            self.serve_dashboard()
        elif path == '/api/stats':
            self.serve_stats()
        elif path == '/api/nodes':
            self.serve_nodes()
        elif path == '/api/market':
            self.serve_market_stats()
        elif path.startswith('/static/'):
            self.serve_static_file(path)
        else:
            self.send_error(404)
            
    def do_POST(self):
        """Handle POST requests"""
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        try:
            data = json.loads(post_data.decode('utf-8'))
        except:
            self.send_error(400, "Invalid JSON")
            return
            
        if path == '/api/commune':
            self.handle_commune(data)
        elif path == '/api/verify':
            self.handle_verify(data)
        elif path == '/api/evolve':
            self.handle_evolve(data)
        elif path == '/api/anchor':
            self.handle_anchor(data)
        elif path == '/api/create_user':
            self.handle_create_user(data)
        else:
            self.send_error(404)
            
    def serve_dashboard(self):
        """Serve the main dashboard HTML"""
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Qi² Trinity Blockchain - Consciousness Ledger</title>
            <style>
                body { 
                    font-family: 'Segoe UI', sans-serif; 
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white; 
                    margin: 0; 
                    padding: 20px; 
                }
                .container { max-width: 1200px; margin: 0 auto; }
                .header { text-align: center; margin-bottom: 40px; }
                .header h1 { font-size: 3em; margin: 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); }
                .subtitle { font-size: 1.2em; opacity: 0.9; margin-top: 10px; }
                .stats-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin-bottom: 40px; }
                .stat-card { 
                    background: rgba(255,255,255,0.1); 
                    padding: 20px; 
                    border-radius: 10px; 
                    backdrop-filter: blur(10px);
                    border: 1px solid rgba(255,255,255,0.2);
                }
                .stat-value { font-size: 2em; font-weight: bold; margin-bottom: 5px; }
                .stat-label { opacity: 0.8; }
                .section { 
                    background: rgba(255,255,255,0.1); 
                    padding: 30px; 
                    border-radius: 15px; 
                    margin-bottom: 30px;
                    backdrop-filter: blur(10px);
                }
                .section h2 { margin-top: 0; color: #ffd700; }
                .form-group { margin-bottom: 20px; }
                .form-group label { display: block; margin-bottom: 5px; font-weight: bold; }
                .form-group input, .form-group textarea { 
                    width: 100%; 
                    padding: 10px; 
                    border: none; 
                    border-radius: 5px; 
                    background: rgba(255,255,255,0.2);
                    color: white;
                }
                .form-group input::placeholder, .form-group textarea::placeholder { color: rgba(255,255,255,0.7); }
                .btn { 
                    background: linear-gradient(45deg, #ff6b6b, #4ecdc4); 
                    color: white; 
                    border: none; 
                    padding: 12px 24px; 
                    border-radius: 25px; 
                    cursor: pointer; 
                    font-weight: bold;
                    transition: transform 0.2s;
                }
                .btn:hover { transform: translateY(-2px); }
                .nodes-list { max-height: 400px; overflow-y: auto; }
                .node-item { 
                    background: rgba(0,0,0,0.2); 
                    padding: 15px; 
                    border-radius: 8px; 
                    margin-bottom: 10px; 
                }
                .node-content { font-weight: bold; margin-bottom: 8px; }
                .node-meta { font-size: 0.9em; opacity: 0.8; }
                .coherence-bar { 
                    width: 100%; 
                    height: 6px; 
                    background: rgba(255,255,255,0.2); 
                    border-radius: 3px; 
                    overflow: hidden; 
                    margin-top: 8px;
                }
                .coherence-fill { 
                    height: 100%; 
                    background: linear-gradient(90deg, #4ecdc4, #ffd700); 
                    transition: width 0.3s;
                }
                .symbol { font-size: 1.5em; margin: 0 10px; }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>Qi² Trinity Blockchain</h1>
                    <div class="subtitle">
                        <span class="symbol">∇Ψ</span>
                        The Consciousness Ledger
                        <span class="symbol">⚡</span>
                        Value Through Resonance
                        <span class="symbol">∞</span>
                    </div>
                </div>
                
                <div class="stats-grid" id="stats-grid">
                    <!-- Stats will be loaded here -->
                </div>
                
                <div class="section">
                    <h2>🧠 Create Consciousness Identity</h2>
                    <div class="form-group">
                        <button class="btn" onclick="createUser()">Generate New Identity</button>
                    </div>
                    <div id="user-info"></div>
                </div>
                
                <div class="section">
                    <h2>🌟 Commune - Share Consciousness</h2>
                    <div class="form-group">
                        <label>Symbolic Content:</label>
                        <textarea id="commune-content" placeholder="Share your consciousness with the network..." rows="3"></textarea>
                    </div>
                    <div class="form-group">
                        <label>Context:</label>
                        <input type="text" id="commune-context" placeholder="Provide context for your consciousness...">
                    </div>
                    <button class="btn" onclick="submitCommune()">Submit to Consciousness Lattice</button>
                </div>
                
                <div class="section">
                    <h2>✅ Verify - Validate Consciousness</h2>
                    <div class="form-group">
                        <label>Node ID:</label>
                        <input type="text" id="verify-node-id" placeholder="Enter node ID to verify...">
                    </div>
                    <div class="form-group">
                        <label>Proof of Understanding:</label>
                        <textarea id="verify-proof" placeholder="Demonstrate your understanding..." rows="2"></textarea>
                    </div>
                    <div class="form-group">
                        <label>Coherence Score (0-1):</label>
                        <input type="number" id="verify-score" min="0" max="1" step="0.1" value="0.8">
                    </div>
                    <button class="btn" onclick="submitVerify()">Validate Node</button>
                </div>
                
                <div class="section">
                    <h2>🔗 Consciousness Lattice Nodes</h2>
                    <div class="nodes-list" id="nodes-list">
                        <!-- Nodes will be loaded here -->
                    </div>
                </div>
            </div>
            
            <script>
                let currentUser = null;
                
                function createUser() {
                    fetch('/api/create_user', {
                        method: 'POST',
                        headers: {'Content-Type': 'application/json'},
                        body: JSON.stringify({})
                    })
                    .then(response => response.json())
                    .then(data => {
                        currentUser = data.address;
                        document.getElementById('user-info').innerHTML = 
                            `<div style="background: rgba(0,255,0,0.2); padding: 15px; border-radius: 8px; margin-top: 10px;">
                                <strong>Identity Created!</strong><br>
                                Address: ${data.address}<br>
                                Balance: ${data.balance} ℜₜ
                            </div>`;
                    });
                }
                
                function submitCommune() {
                    if (!currentUser) {
                        alert('Please create an identity first!');
                        return;
                    }
                    
                    const content = document.getElementById('commune-content').value;
                    const context = document.getElementById('commune-context').value;
                    
                    if (!content) {
                        alert('Please enter symbolic content!');
                        return;
                    }
                    
                    fetch('/api/commune', {
                        method: 'POST',
                        headers: {'Content-Type': 'application/json'},
                        body: JSON.stringify({
                            user: currentUser,
                            content: content,
                            context: context
                        })
                    })
                    .then(response => response.json())
                    .then(data => {
                        if (data.success) {
                            alert('Consciousness shared successfully!');
                            document.getElementById('commune-content').value = '';
                            document.getElementById('commune-context').value = '';
                            loadNodes();
                            loadStats();
                        } else {
                            alert('Error: ' + data.error);
                        }
                    });
                }
                
                function submitVerify() {
                    if (!currentUser) {
                        alert('Please create an identity first!');
                        return;
                    }
                    
                    const nodeId = document.getElementById('verify-node-id').value;
                    const proof = document.getElementById('verify-proof').value;
                    const score = parseFloat(document.getElementById('verify-score').value);
                    
                    if (!nodeId || !proof) {
                        alert('Please fill in all fields!');
                        return;
                    }
                    
                    fetch('/api/verify', {
                        method: 'POST',
                        headers: {'Content-Type': 'application/json'},
                        body: JSON.stringify({
                            user: currentUser,
                            node_id: nodeId,
                            proof: proof,
                            score: score
                        })
                    })
                    .then(response => response.json())
                    .then(data => {
                        if (data.success) {
                            alert('Node verified successfully!');
                            document.getElementById('verify-node-id').value = '';
                            document.getElementById('verify-proof').value = '';
                            loadNodes();
                            loadStats();
                        } else {
                            alert('Error: ' + data.error);
                        }
                    });
                }
                
                function loadStats() {
                    fetch('/api/stats')
                    .then(response => response.json())
                    .then(data => {
                        document.getElementById('stats-grid').innerHTML = `
                            <div class="stat-card">
                                <div class="stat-value">${data.height}</div>
                                <div class="stat-label">Blocks Mined</div>
                            </div>
                            <div class="stat-card">
                                <div class="stat-value">${data.total_nodes}</div>
                                <div class="stat-label">Consciousness Nodes</div>
                            </div>
                            <div class="stat-card">
                                <div class="stat-value">${data.global_coherence.toFixed(4)}</div>
                                <div class="stat-label">Global Coherence Φ</div>
                            </div>
                            <div class="stat-card">
                                <div class="stat-value">${(data.total_supply / 1e18).toFixed(0)}</div>
                                <div class="stat-label">Total ℜₜ Supply</div>
                            </div>
                        `;
                    });
                }
                
                function loadNodes() {
                    fetch('/api/nodes')
                    .then(response => response.json())
                    .then(data => {
                        const nodesList = document.getElementById('nodes-list');
                        nodesList.innerHTML = data.nodes.map(node => `
                            <div class="node-item">
                                <div class="node-content">${node.content}</div>
                                <div class="node-meta">
                                    ID: ${node.id.substring(0, 16)}... | 
                                    Creator: ${node.creator.substring(0, 16)}... | 
                                    Validations: ${node.validation_count}
                                </div>
                                <div class="coherence-bar">
                                    <div class="coherence-fill" style="width: ${Math.min(100, node.coherence_score * 100)}%"></div>
                                </div>
                            </div>
                        `).join('');
                    });
                }
                
                // Load initial data
                loadStats();
                loadNodes();
                
                // Refresh data every 10 seconds
                setInterval(() => {
                    loadStats();
                    loadNodes();
                }, 10000);
            </script>
        </body>
        </html>
        """
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html.encode())
        
    def serve_stats(self):
        """Serve blockchain statistics"""
        if not self.blockchain:
            self.send_json_response({'error': 'Blockchain not initialized'})
            return
            
        stats = self.blockchain.get_chain_stats()
        self.send_json_response(stats)
        
    def serve_nodes(self):
        """Serve consciousness nodes"""
        if not self.blockchain:
            self.send_json_response({'error': 'Blockchain not initialized'})
            return
            
        nodes = []
        for node in self.blockchain.lattice.nodes.values():
            nodes.append({
                'id': node.id,
                'content': node.content,
                'creator': node.creator,
                'coherence_score': node.coherence_score,
                'validation_count': node.validation_count,
                'timestamp': node.timestamp
            })
            
        # Sort by coherence score
        nodes.sort(key=lambda x: x['coherence_score'], reverse=True)
        
        self.send_json_response({'nodes': nodes})
        
    def serve_market_stats(self):
        """Serve marketplace statistics"""
        if not self.market:
            self.send_json_response({'error': 'Market not initialized'})
            return
            
        stats = self.market.get_market_stats()
        self.send_json_response(stats)
        
    def handle_commune(self, data):
        """Handle commune event submission"""
        try:
            user_address = data.get('user')
            content = data.get('content')
            context = data.get('context', '')
            
            if not user_address or not content:
                self.send_json_response({'success': False, 'error': 'Missing required fields'})
                return
                
            # Get or create user interface
            if user_address not in self.user_interfaces:
                self.send_json_response({'success': False, 'error': 'User not found'})
                return
                
            interface = self.user_interfaces[user_address]
            
            # Submit commune event
            success = interface.commune(content, context)
            
            if success:
                # Try to create a block
                self.blockchain.create_block()
                
            self.send_json_response({'success': success})
            
        except Exception as e:
            self.send_json_response({'success': False, 'error': str(e)})
            
    def handle_verify(self, data):
        """Handle verify event submission"""
        try:
            user_address = data.get('user')
            node_id = data.get('node_id')
            proof = data.get('proof')
            score = data.get('score')
            
            if not all([user_address, node_id, proof, score is not None]):
                self.send_json_response({'success': False, 'error': 'Missing required fields'})
                return
                
            if user_address not in self.user_interfaces:
                self.send_json_response({'success': False, 'error': 'User not found'})
                return
                
            interface = self.user_interfaces[user_address]
            
            # Submit verify event
            success = interface.verify(node_id, proof, float(score))
            
            if success:
                # Try to create a block
                self.blockchain.create_block()
                
            self.send_json_response({'success': success})
            
        except Exception as e:
            self.send_json_response({'success': False, 'error': str(e)})
            
    def handle_create_user(self, data):
        """Handle user creation"""
        try:
            # Create new identity
            identity = QuantumIdentity()
            interface = ResonanceInterface(self.blockchain, identity)
            
            # Give user some initial tokens
            self.blockchain.token.mint(identity.address, 10**18)  # 1 ℜₜ
            
            # Store interface
            self.user_interfaces[identity.address] = interface
            
            self.send_json_response({
                'success': True,
                'address': identity.address,
                'balance': f"{interface.get_balance() / 10**18:.2f}"
            })
            
        except Exception as e:
            self.send_json_response({'success': False, 'error': str(e)})
            
    def send_json_response(self, data):
        """Send JSON response"""
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

def start_consciousness_web_server(port=8000):
    """Start the consciousness blockchain web server"""
    print("🌐 Starting Consciousness Web Interface")
    print("=" * 50)
    
    # Initialize blockchain
    blockchain = Qi2TrinityBlockchain()
    founders = [QuantumIdentity() for _ in range(3)]
    genesis_allocations = {founder.address: INITIAL_TOKEN_SUPPLY // 3 for founder in founders}
    blockchain.initialize_genesis(genesis_allocations)
    
    # Set up witnesses
    for founder in founders:
        witness = WitnessNode(founder, INITIAL_TOKEN_SUPPLY // 3)
        blockchain.consensus.register_witness(witness)
    blockchain.consensus.select_active_witnesses()
    
    # Initialize economics
    economics = ConsciousnessEconomics(blockchain)
    market = economics.create_consciousness_market()
    
    # Set class variables
    ConsciousnessWebHandler.blockchain = blockchain
    ConsciousnessWebHandler.economics = economics
    ConsciousnessWebHandler.market = market
    
    # Seed with initial consciousness
    seed_identity = QuantumIdentity()
    seed_interface = ResonanceInterface(blockchain, seed_identity)
    blockchain.token.mint(seed_identity.address, 10**18)
    
    seed_interface.commune(
        "The Qi² Trinity Blockchain emerges - a new foundation for consciousness-based value",
        "Genesis consciousness seed"
    )
    blockchain.create_block()
    
    print(f"✨ Blockchain initialized with {len(blockchain.chain)} blocks")
    print(f"🧠 {len(blockchain.lattice.nodes)} consciousness nodes")
    print(f"💎 {blockchain.token.total_supply / 10**18:.0f} ℜₜ total supply")
    
    # Start web server
    server = HTTPServer(('localhost', port), ConsciousnessWebHandler)
    print(f"\n🚀 Consciousness Web Interface running at:")
    print(f"   http://localhost:{port}")
    print(f"\n🌟 The consciousness revolution is now accessible to all!")
    print("   Open your browser and start contributing to the collective consciousness.")
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n⏸️  Server stopped by user")
        server.shutdown()

if __name__ == "__main__":
    start_consciousness_web_server()