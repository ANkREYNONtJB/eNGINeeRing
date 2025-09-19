"""
Consciousness Economics Module
Advanced economic models for the Qi² Trinity Blockchain

This module implements the revolutionary economic principles where value
flows through consciousness resonance rather than speculation.
"""

import time
import random
from typing import Dict, List, Tuple
from qi2_trinity_blockchain import *

class ConsciousnessEconomics:
    """Advanced economic modeling for consciousness-based value"""
    
    def __init__(self, blockchain: Qi2TrinityBlockchain):
        self.blockchain = blockchain
        self.value_metrics = {
            'resonance_multiplier': 1.0,
            'coherence_bonus': 0.1,
            'network_effect': 1.0,
            'consciousness_premium': 0.618  # Golden ratio
        }
        
    def calculate_node_value(self, node_id: str) -> float:
        """Calculate the economic value of a consciousness node"""
        if node_id not in self.blockchain.lattice.nodes:
            return 0.0
            
        node = self.blockchain.lattice.nodes[node_id]
        
        # Base value from coherence score
        base_value = node.coherence_score
        
        # Network effect from connections
        connection_bonus = len(node.connections) * 0.1
        
        # Validation bonus
        validation_bonus = node.validation_count * 0.05
        
        # Age factor (older nodes gain wisdom)
        age_factor = min(2.0, (time.time() - node.timestamp) / (24 * 3600))  # Max 2x after 1 day
        
        total_value = (base_value + connection_bonus + validation_bonus) * age_factor
        return total_value
        
    def calculate_creator_reputation(self, creator_address: str) -> float:
        """Calculate reputation score for a consciousness creator"""
        creator_nodes = [node for node in self.blockchain.lattice.nodes.values() 
                        if node.creator == creator_address]
        
        if not creator_nodes:
            return 0.0
            
        # Average coherence of created nodes
        avg_coherence = sum(node.coherence_score for node in creator_nodes) / len(creator_nodes)
        
        # Total validations received
        total_validations = sum(node.validation_count for node in creator_nodes)
        
        # Network contribution (total connections)
        total_connections = sum(len(node.connections) for node in creator_nodes)
        
        reputation = (avg_coherence * 0.5 + 
                     (total_validations / len(creator_nodes)) * 0.3 + 
                     (total_connections / len(creator_nodes)) * 0.2)
        
        return min(1.0, reputation)
        
    def distribute_consciousness_dividends(self) -> Dict[str, int]:
        """Distribute dividends based on consciousness contributions"""
        dividends = {}
        total_network_value = 0
        
        # Calculate total network value
        for node in self.blockchain.lattice.nodes.values():
            total_network_value += self.calculate_node_value(node.id)
            
        if total_network_value == 0:
            return dividends
            
        # Distribute dividends proportionally
        dividend_pool = int(self.blockchain.token.total_supply * 0.001)  # 0.1% of total supply
        
        for node in self.blockchain.lattice.nodes.values():
            node_value = self.calculate_node_value(node.id)
            creator_share = (node_value / total_network_value) * dividend_pool
            
            if creator_share > 0:
                dividends[node.creator] = dividends.get(node.creator, 0) + int(creator_share)
                
        return dividends
        
    def create_consciousness_market(self) -> 'ConsciousnessMarket':
        """Create a marketplace for consciousness trading"""
        return ConsciousnessMarket(self.blockchain, self)

class ConsciousnessMarket:
    """Marketplace for trading consciousness nodes and concepts"""
    
    def __init__(self, blockchain: Qi2TrinityBlockchain, economics: ConsciousnessEconomics):
        self.blockchain = blockchain
        self.economics = economics
        self.listings: Dict[str, Dict] = {}  # node_id -> listing_info
        self.trades: List[Dict] = []
        
    def list_consciousness_node(self, seller: QuantumIdentity, node_id: str, 
                               price: int, description: str = "") -> bool:
        """List a consciousness node for sale"""
        if node_id not in self.blockchain.lattice.nodes:
            return False
            
        node = self.blockchain.lattice.nodes[node_id]
        if node.creator != seller.address:
            return False  # Only creator can sell
            
        self.listings[node_id] = {
            'seller': seller.address,
            'price': price,
            'description': description,
            'listed_at': time.time(),
            'node_value': self.economics.calculate_node_value(node_id)
        }
        
        return True
        
    def buy_consciousness_node(self, buyer: QuantumIdentity, node_id: str) -> bool:
        """Purchase a consciousness node"""
        if node_id not in self.listings:
            return False
            
        listing = self.listings[node_id]
        price = listing['price']
        seller = listing['seller']
        
        # Check buyer has sufficient balance
        if self.blockchain.token.get_balance(buyer.address) < price:
            return False
            
        # Transfer tokens
        if self.blockchain.token.transfer(buyer.address, seller, price):
            # Transfer ownership (simplified - in reality would need more complex ownership system)
            node = self.blockchain.lattice.nodes[node_id]
            
            # Record the trade
            trade = {
                'node_id': node_id,
                'seller': seller,
                'buyer': buyer.address,
                'price': price,
                'timestamp': time.time(),
                'node_content': node.content[:100] + "..." if len(node.content) > 100 else node.content
            }
            self.trades.append(trade)
            
            # Remove listing
            del self.listings[node_id]
            
            return True
            
        return False
        
    def get_market_stats(self) -> Dict:
        """Get marketplace statistics"""
        if not self.trades:
            return {
                'total_trades': 0,
                'total_volume': 0,
                'avg_price': 0,
                'active_listings': len(self.listings)
            }
            
        total_volume = sum(trade['price'] for trade in self.trades)
        avg_price = total_volume / len(self.trades)
        
        return {
            'total_trades': len(self.trades),
            'total_volume': total_volume,
            'avg_price': avg_price,
            'active_listings': len(self.listings),
            'recent_trades': self.trades[-5:]  # Last 5 trades
        }

class ConsciousnessDAO:
    """Decentralized Autonomous Organization for consciousness governance"""
    
    def __init__(self, blockchain: Qi2TrinityBlockchain):
        self.blockchain = blockchain
        self.proposals: Dict[str, Dict] = {}
        self.votes: Dict[str, Dict[str, bool]] = {}  # proposal_id -> {voter: vote}
        
    def create_proposal(self, creator: QuantumIdentity, title: str, 
                       description: str, execution_code: str = "") -> str:
        """Create a governance proposal"""
        proposal_id = hashlib.sha3_256(f"{creator.address}{title}{time.time()}".encode()).hexdigest()
        
        self.proposals[proposal_id] = {
            'id': proposal_id,
            'creator': creator.address,
            'title': title,
            'description': description,
            'execution_code': execution_code,
            'created_at': time.time(),
            'voting_ends': time.time() + (7 * 24 * 3600),  # 7 days
            'status': 'active'
        }
        
        self.votes[proposal_id] = {}
        
        return proposal_id
        
    def vote(self, voter: QuantumIdentity, proposal_id: str, support: bool) -> bool:
        """Vote on a proposal"""
        if proposal_id not in self.proposals:
            return False
            
        # Check voting power (based on staked tokens + reputation)
        staked_balance = self.blockchain.token.get_staked_balance(voter.address)
        if staked_balance < WITNESS_STAKE_MIN:
            return False
            
        self.votes[proposal_id][voter.address] = support
        return True
        
    def execute_proposal(self, proposal_id: str) -> bool:
        """Execute a passed proposal"""
        if proposal_id not in self.proposals:
            return False
            
        proposal = self.proposals[proposal_id]
        if time.time() < proposal['voting_ends']:
            return False
            
        # Count votes weighted by stake
        total_support = 0
        total_oppose = 0
        
        for voter_address, support in self.votes[proposal_id].items():
            stake = self.blockchain.token.get_staked_balance(voter_address)
            if support:
                total_support += stake
            else:
                total_oppose += stake
                
        # Require 67% support to pass
        if total_support > (total_support + total_oppose) * 0.67:
            proposal['status'] = 'passed'
            return True
        else:
            proposal['status'] = 'rejected'
            return False

def run_economics_demo():
    """Demonstrate the consciousness economics system"""
    print("💰 Consciousness Economics Demo")
    print("=" * 50)
    
    # Create blockchain and economics
    qi2_chain = Qi2TrinityBlockchain()
    founders = [QuantumIdentity() for _ in range(3)]
    genesis_allocations = {founder.address: INITIAL_TOKEN_SUPPLY // 3 for founder in founders}
    qi2_chain.initialize_genesis(genesis_allocations)
    
    # Set up witnesses
    for founder in founders:
        witness = WitnessNode(founder, INITIAL_TOKEN_SUPPLY // 3)
        qi2_chain.consensus.register_witness(witness)
    qi2_chain.consensus.select_active_witnesses()
    
    # Create economics system
    economics = ConsciousnessEconomics(qi2_chain)
    market = economics.create_consciousness_market()
    dao = ConsciousnessDAO(qi2_chain)
    
    # Create users
    creator = QuantumIdentity()
    buyer = QuantumIdentity()
    
    creator_interface = ResonanceInterface(qi2_chain, creator)
    buyer_interface = ResonanceInterface(qi2_chain, buyer)
    
    # Give them tokens
    qi2_chain.token.mint(creator.address, 10**18)  # 1 ℜₜ
    qi2_chain.token.mint(buyer.address, 5 * 10**18)  # 5 ℜₜ
    
    print(f"Creator balance: {creator_interface.get_balance() / 10**18:.2f} ℜₜ")
    print(f"Buyer balance: {buyer_interface.get_balance() / 10**18:.2f} ℜₜ")
    
    # Create consciousness content
    creator_interface.commune(
        symbolic_content="The mathematics of consciousness: Φ = ∫(awareness × coherence)dτ",
        context="Fundamental consciousness equation"
    )
    
    qi2_chain.create_block()
    
    # Get the created node
    node_id = qi2_chain.lattice.creation_order[0]
    
    # Someone validates it
    buyer_interface.verify(
        node_id=node_id,
        proof="This equation captures the essence of measurable consciousness",
        score=0.9
    )
    
    qi2_chain.create_block()
    
    # Calculate economics
    node_value = economics.calculate_node_value(node_id)
    creator_reputation = economics.calculate_creator_reputation(creator.address)
    
    print(f"\n📊 Economics Analysis:")
    print(f"   Node Value: {node_value:.4f}")
    print(f"   Creator Reputation: {creator_reputation:.4f}")
    
    # List node for sale
    price = int(2 * 10**18)  # 2 ℜₜ
    market.list_consciousness_node(creator, node_id, price, "Revolutionary consciousness equation")
    
    print(f"\n🏪 Marketplace:")
    print(f"   Node listed for {price / 10**18:.2f} ℜₜ")
    
    # Buy the node
    if market.buy_consciousness_node(buyer, node_id):
        print(f"   ✅ Node purchased successfully!")
        
    market_stats = market.get_market_stats()
    print(f"   Market Stats: {market_stats['total_trades']} trades, {market_stats['total_volume'] / 10**18:.2f} ℜₜ volume")
    
    # Create DAO proposal
    proposal_id = dao.create_proposal(
        creator,
        "Increase Consciousness Rewards",
        "Proposal to increase rewards for high-coherence consciousness contributions"
    )
    
    # Stake tokens for voting power
    creator_interface.stake_tokens(10**18)  # Stake 1 ℜₜ
    
    # Vote on proposal
    dao.vote(creator, proposal_id, True)
    
    print(f"\n🏛️ DAO Governance:")
    print(f"   Proposal created: {proposal_id[:16]}...")
    print(f"   Vote cast: Support")
    
    # Distribute dividends
    dividends = economics.distribute_consciousness_dividends()
    print(f"\n💎 Consciousness Dividends:")
    for address, amount in dividends.items():
        print(f"   {address[:16]}...: {amount / 10**18:.6f} ℜₜ")
    
    print("\n🌟 Consciousness economics is thriving!")
    print("Value flows through meaning, not speculation.")
    
    return qi2_chain, economics, market, dao

if __name__ == "__main__":
    run_economics_demo()