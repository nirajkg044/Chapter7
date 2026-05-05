"""
LangGraph Bundle Development - Quick Start Examples
9 Complete Examples to Understand the System
"""

import json
from datetime import datetime


# ============================================================================
# EXAMPLE 1: Complete Workflow Execution
# ============================================================================

def example_complete_workflow():
    """
    Run the complete Disney bundle development workflow with self-correction
    """
    from LangGraph import DisneyBundleOrchestrator
    
    print("\n" + "="*80)
    print("EXAMPLE 1: Complete Workflow Execution")
    print("="*80)
    
    orchestrator = DisneyBundleOrchestrator()
    
    # Execute complete workflow
    workflow_result = orchestrator.run_bundle_development_workflow()
    
    # Print summary
    print(f"\n✓ Workflow completed in {workflow_result['iterations_completed']} iterations")
    print(f"✓ Total potential iterations: {workflow_result['total_iterations']}")
    
    return workflow_result


# ============================================================================
# EXAMPLE 2: Market Research Only
# ============================================================================

def example_market_research():
    """
    Use MarketResearchAgent to analyze competitors
    """
    from LangGraph import MarketResearchAgent, BundleDatabase
    
    print("\n" + "="*80)
    print("EXAMPLE 2: Market Research Analysis")
    print("="*80)
    
    db = BundleDatabase()
    market_agent = MarketResearchAgent(db)
    
    # Get competitor bundles
    competitors = market_agent.get_competitor_bundles()
    
    print(f"\n✓ Competitor Analysis Complete")
    print(f"✓ Competitors analyzed: {len(competitors)}")
    
    # Generate report
    report = market_agent.generate_market_research_report()
    
    print(f"\n📊 Market Insights:")
    print(f"  Total competitor users: {report['total_competitor_users']:,}")
    print(f"  Average bundle price: ${report['average_bundle_price']:.2f}/month")
    print(f"  Market gaps identified: {len(report['market_gaps']['service_combinations'])} opportunities")
    
    return report


# ============================================================================
# EXAMPLE 3: User Persona Analysis
# ============================================================================

def example_persona_analysis():
    """
    Use PersonaAnalysisAgent to understand user segments
    """
    from LangGraph import PersonaAnalysisAgent, BundleDatabase
    
    print("\n" + "="*80)
    print("EXAMPLE 3: User Persona Analysis")
    print("="*80)
    
    db = BundleDatabase()
    persona_agent = PersonaAnalysisAgent(db)
    
    # Analyze segments
    personas = persona_agent.analyze_user_segments()
    
    print(f"\n✓ Persona Analysis Complete")
    print(f"✓ Personas identified: {len(personas)}")
    
    # Generate report
    report = persona_agent.generate_persona_report()
    
    print(f"\n👥 Persona Insights:")
    print(f"  Total addressable market: {report['total_addressable_market']:,} users")
    print(f"  Avg willingness to pay: ${report['average_willingness_to_pay']:.2f}")
    
    print(f"\n  Persona breakdown:")
    for persona in personas:
        print(f"    - {persona.name}: {persona.estimated_segment_size:,} users (${persona.willingness_to_pay}/mo)")
    
    return report


# ============================================================================
# EXAMPLE 4: Bundle Generation
# ============================================================================

def example_bundle_generation():
    """
    Use OfferIdeationAgent to generate bundle concepts
    """
    from LangGraph import (
        OfferIdeationAgent,
        MarketResearchAgent,
        PersonaAnalysisAgent,
        BundleDatabase
    )
    
    print("\n" + "="*80)
    print("EXAMPLE 4: Bundle Concept Generation")
    print("="*80)
    
    db = BundleDatabase()
    
    # Get market and persona data first
    market_agent = MarketResearchAgent(db)
    market_report = market_agent.generate_market_research_report()
    
    persona_agent = PersonaAnalysisAgent(db)
    persona_report = persona_agent.generate_persona_report()
    
    # Generate bundles
    ideation_agent = OfferIdeationAgent(db, iteration_count=0)
    bundles = ideation_agent.generate_bundle_concepts(market_report, persona_report)
    
    print(f"\n✓ Bundle Generation Complete")
    print(f"✓ Bundles generated: {len(bundles)}")
    
    print(f"\n💡 Generated Bundles:")
    for bundle in bundles:
        print(f"  - {bundle.name}")
        print(f"    Services: {', '.join(bundle.services)}")
        print(f"    Price: ${bundle.final_price}/month (was ${bundle.base_price})")
        print(f"    Target personas: {len(bundle.target_personas)}")
        print()
    
    return bundles


# ============================================================================
# EXAMPLE 5: Simulation & Uptake Prediction
# ============================================================================

def example_simulation():
    """
    Use SimulationAgent to predict user uptake
    """
    from LangGraph import (
        SimulationAgent,
        MarketResearchAgent,
        PersonaAnalysisAgent,
        OfferIdeationAgent,
        BundleDatabase
    )
    
    print("\n" + "="*80)
    print("EXAMPLE 5: Bundle Simulation & Uptake Prediction")
    print("="*80)
    
    db = BundleDatabase()
    
    # Prepare data
    market_agent = MarketResearchAgent(db)
    market_report = market_agent.generate_market_research_report()
    
    persona_agent = PersonaAnalysisAgent(db)
    personas = persona_agent.analyze_user_segments()
    persona_report = persona_agent.generate_persona_report()
    
    ideation_agent = OfferIdeationAgent(db)
    bundles = ideation_agent.generate_bundle_concepts(market_report, persona_report)
    
    # Simulate each bundle
    simulation_agent = SimulationAgent(db)
    results = []
    
    for bundle in bundles:
        result = simulation_agent.simulate_bundle_uptake(bundle, personas)
        results.append(result)
    
    print(f"\n✓ Simulation Complete")
    print(f"✓ Bundles simulated: {len(results)}")
    
    # Summary
    print(f"\n📈 Simulation Results Summary:")
    for result in results:
        status = "✅ APPROVED" if result['overall_estimated_uptake'] >= 35 else "⚠️ NEEDS REVISION"
        print(f"  {result['bundle_name']}")
        print(f"    Uptake: {result['overall_estimated_uptake']:.1f}% {status}")
        print(f"    Revenue: ${result['annual_revenue_projection']:,.0f}/year")
    
    return results


# ============================================================================
# EXAMPLE 6: Self-Correction Analysis
# ============================================================================

def example_self_correction():
    """
    Use SelfCorrectionAgent to handle low uptake
    """
    from LangGraph import (
        SelfCorrectionAgent,
        SimulationAgent,
        MarketResearchAgent,
        PersonaAnalysisAgent,
        OfferIdeationAgent,
        BundleDatabase
    )
    
    print("\n" + "="*80)
    print("EXAMPLE 6: Self-Correction Analysis")
    print("="*80)
    
    db = BundleDatabase()
    
    # Prepare and simulate
    market_agent = MarketResearchAgent(db)
    market_report = market_agent.generate_market_research_report()
    
    persona_agent = PersonaAnalysisAgent(db)
    personas = persona_agent.analyze_user_segments()
    persona_report = persona_agent.generate_persona_report()
    
    ideation_agent = OfferIdeationAgent(db)
    bundles = ideation_agent.generate_bundle_concepts(market_report, persona_report)
    
    simulation_agent = SimulationAgent(db)
    
    # Simulate and check for low uptake
    correction_agent = SelfCorrectionAgent(db)
    
    for bundle in bundles[:2]:  # Check first 2 bundles
        result = simulation_agent.simulate_bundle_uptake(bundle, personas)
        
        print(f"\n📊 Analyzing: {bundle.name}")
        print(f"   Current Uptake: {result['overall_estimated_uptake']:.1f}%")
        
        # Analyze if correction needed
        analysis = correction_agent.analyze_low_uptake(result)
        
        if analysis['needs_correction']:
            print(f"   ⚠️  Correction needed!")
            print(f"   Issues found: {len(analysis['correction_opportunities'])}")
            for opportunity in analysis['correction_opportunities']:
                print(f"     - {opportunity['issue']}")
            print(f"   Recommended path: {analysis['recommended_iteration']}")
        else:
            print(f"   ✅ Uptake acceptable - No correction needed")


# ============================================================================
# EXAMPLE 7: Full Iteration Cycle
# ============================================================================

def example_iteration_cycle():
    """
    Show how bundles improve across iterations
    """
    from LangGraph import OfferIdeationAgent, BundleDatabase
    
    print("\n" + "="*80)
    print("EXAMPLE 7: Bundle Improvement Across Iterations")
    print("="*80)
    
    db = BundleDatabase()
    
    print("\nSimulating bundle improvement across iterations:")
    print()
    
    iterations = 3
    for i in range(iterations):
        ideation_agent = OfferIdeationAgent(db, iteration_count=i)
        bundles = ideation_agent.generated_bundles
        
        if not bundles or i == 0:
            # Generate bundles for iteration
            from LangGraph import MarketResearchAgent, PersonaAnalysisAgent
            market_agent = MarketResearchAgent(db)
            market_report = market_agent.generate_market_research_report()
            persona_agent = PersonaAnalysisAgent(db)
            persona_report = persona_agent.generate_persona_report()
            
            ideation_agent = OfferIdeationAgent(db, iteration_count=i)
            bundles = ideation_agent.generate_bundle_concepts(market_report, persona_report)
        
        print(f"Iteration {i + 1}:")
        for bundle in bundles[:2]:
            print(f"  {bundle.name}: {bundle.estimated_uptake:.1f}% estimated uptake")
        print()


# ============================================================================
# EXAMPLE 8: Database Querying
# ============================================================================

def example_database_queries():
    """
    Query the SQLite database directly
    """
    from LangGraph import BundleDatabase
    
    print("\n" + "="*80)
    print("EXAMPLE 8: Database Queries")
    print("="*80)
    
    db = BundleDatabase()
    
    # Query 1: Top competitors by market share
    print("\n1️⃣ Top Competitors by Market Share:")
    query = """
        SELECT name, price_per_month, market_share_percent, estimated_users
        FROM competitor_bundles
        ORDER BY market_share_percent DESC
        LIMIT 3
    """
    results = db.execute_query(query)
    for row in results:
        print(f"   {row[0]}: {row[3]:,} users ({row[2]}% share)")
    
    # Query 2: Persona willingness to pay
    print("\n2️⃣ User Segment WTP (Willingness to Pay):")
    query = "SELECT name, willingness_to_pay FROM user_personas ORDER BY willingness_to_pay DESC"
    results = db.execute_query(query)
    for row in results:
        print(f"   {row[0]}: ${row[1]:.2f}/month")
    
    # Query 3: Best performing bundles
    print("\n3️⃣ Best Performing Bundles:")
    query = """
        SELECT name, estimated_uptake, revenue_potential
        FROM bundle_proposals
        WHERE status = 'PROPOSED'
        ORDER BY estimated_uptake DESC
        LIMIT 3
    """
    results = db.execute_query(query)
    for row in results:
        print(f"   {row[0]}: {row[1]:.1f}% uptake, ${row[2]:,.0f} potential")


# ============================================================================
# EXAMPLE 9: Executive Summary Report
# ============================================================================

def example_executive_report():
    """
    Generate executive summary of bundle strategy
    """
    from LangGraph import DisneyBundleOrchestrator
    
    print("\n" + "="*80)
    print("EXAMPLE 9: Executive Summary Report")
    print("="*80)
    
    orchestrator = DisneyBundleOrchestrator()
    workflow_result = orchestrator.run_bundle_development_workflow()
    
    # Generate strategy document
    strategy_doc = orchestrator.generate_strategy_document(workflow_result)
    
    print("\n" + strategy_doc)


# ============================================================================
# EXAMPLE 10: Custom Bundle Analysis
# ============================================================================

def example_custom_bundle():
    """
    Analyze a custom bundle configuration
    """
    from LangGraph import (
        BundleProposal,
        SimulationAgent,
        PersonaAnalysisAgent,
        BundleDatabase
    )
    from datetime import datetime
    
    print("\n" + "="*80)
    print("EXAMPLE 10: Custom Bundle Analysis")
    print("="*80)
    
    db = BundleDatabase()
    
    # Create custom bundle
    custom_bundle = BundleProposal(
        bundle_id="CUSTOM_001",
        name="Disney+ Sports Entertainment Bundle",
        services=["Disney+", "ESPN+", "Hulu", "ESPN3"],
        base_price=49.99,
        discount_percent=20,
        final_price=39.99,
        target_personas=["SPORTS_ENTHUSIAST", "FAMILY_ORIENTED", "PREMIUM_USER"],
        estimated_uptake=0,
        revenue_potential=0,
        iteration_count=0,
        created_at=datetime.now().isoformat()
    )
    
    print(f"\n📦 Custom Bundle Created:")
    print(f"   Name: {custom_bundle.name}")
    print(f"   Services: {', '.join(custom_bundle.services)}")
    print(f"   Price: ${custom_bundle.final_price}/month")
    print(f"   Target Personas: {len(custom_bundle.target_personas)}")
    
    # Simulate
    personas = PersonaAnalysisAgent(db).analyze_user_segments()
    simulation_agent = SimulationAgent(db)
    result = simulation_agent.simulate_bundle_uptake(custom_bundle, personas)
    
    print(f"\n📊 Simulation Result:")
    print(f"   Estimated Uptake: {result['overall_estimated_uptake']:.1f}%")
    print(f"   Projected Revenue (Annual): ${result['annual_revenue_projection']:,.0f}")
    print(f"   User Satisfaction: {result['user_satisfaction_score']:.1f}/100")
    print(f"   Recommendation: {result['recommendation']}")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("\n" + "#"*80)
    print("# DISNEY BUNDLE DEVELOPMENT - QUICK START EXAMPLES")
    print("# 10 Complete Examples to Explore the System")
    print("#"*80)
    
    # Uncomment example(s) to run:
    
    # Example 1: Complete workflow
    print("\nRunning Example 1: Complete Workflow\n")
    example_complete_workflow()
    
    # Example 2: Market research
    # print("\nRunning Example 2: Market Research\n")
    # example_market_research()
    
    # Example 3: Persona analysis
    # print("\nRunning Example 3: Persona Analysis\n")
    # example_persona_analysis()
    
    # Example 4: Bundle generation
    # print("\nRunning Example 4: Bundle Generation\n")
    # example_bundle_generation()
    
    # Example 5: Simulation
    # print("\nRunning Example 5: Simulation\n")
    # example_simulation()
    
    # Example 6: Self-correction
    # print("\nRunning Example 6: Self-Correction\n")
    # example_self_correction()
    
    # Example 7: Iteration cycle
    # print("\nRunning Example 7: Iteration Cycle\n")
    # example_iteration_cycle()
    
    # Example 8: Database queries
    # print("\nRunning Example 8: Database Queries\n")
    # example_database_queries()
    
    # Example 9: Executive report
    # print("\nRunning Example 9: Executive Report\n")
    # example_executive_report()
    
    # Example 10: Custom bundle
    # print("\nRunning Example 10: Custom Bundle\n")
    # example_custom_bundle()
    
    print("\n✅ Examples completed!")
