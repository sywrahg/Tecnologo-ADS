package questao02cap03;

public class BalancoTrimestral {
	public static void main(String[] args) {
		int gastosJaneiro = 15000;
		int gastosFevereiro = 23000;
		int gastosMarco = 17000;
		int gastosTrimestre = gastosJaneiro + gastosFevereiro + gastosMarco;
		
		System.out.println("Gastos do trimestre = " + gastosTrimestre);
		
		float mediaMensal = gastosTrimestre / 3;
		
		System.out.println("Valor da m�dia mensal = "+ mediaMensal);
	}
}
