from HextoBinLib import countTheErrorAverageForEachSymbol, innerErrorDistributionCounterForBit 
from HextoBinLib import innerErrorDistributionPercentageForBit , burstErrorCalculatorForBit
import matplotlib.pyplot as plt

def plotter(numberOfBits, resultList, PlotTitle, plotXLabel, pltYLabel, XrangeFrom, XrangeTo, YrangeFrom, YrangeTo):
    # initilizing
    # mu = InputMu
    # sigma = InputSimga
    x = []
    for i in range(numberOfBits):
        x.append(i)

    # innerErrorDistributionPercentage
    # print(innerErrorDistributionPercentage(ListofInnerErrors)) what is it ?
    plt.bar(x, resultList)
    plt.title(PlotTitle)
    plt.xlabel(plotXLabel)
    plt.ylabel(pltYLabel)

    plt.axis([XrangeFrom, XrangeTo, YrangeFrom, YrangeTo])
    plt.grid(True)
    plt.show()

def plotBitErrorDistributionOverAllErrorPatterns(IndiciesOfError):
    '''
    Enter the indicies of error and you'll receive 
    the count errors of each index over all given error patterns
    '''
    answer = innerErrorDistributionCounterForBit(IndiciesOfError)
    print(answer)
    plotter(248,answer,"Bit errors indicies distribution over all packets","indicies","#Errors",0,248,0,400)

def plotBitErrorDistributionOverAllErrorPatternsByPercentage(IndiciesOfError):
    '''
    Enter the indicies of error and it'll calculate
    percentage of errors of each index over all given error patterns
    '''
    answer = innerErrorDistributionPercentageForBit(IndiciesOfError)
    plotter(248,answer,"Percentage of bit errors indicies distribution over all packets","indicies","%Error",0,248,0,1)

def plotBurstErrorCalculatorForBit(list):
    '''
    plots the number of burst errors over all-error-patterns
    '''
    answer = burstErrorCalculatorForBit(list)
    plotter(248,answer,"Total number of burst error over all error patterns","burst lenght","count",0,30,0,15000)

def plotAvgBitErrorPerSymbol(list,totalErrorPattern):
    '''
    For each symbol find the avg of error over all received error pattern
    '''
    errorCountPerIndicies = innerErrorDistributionCounterForBit(list)
    
    answer = countTheErrorAverageForEachSymbol(errorCountPerIndicies,totalErrorPattern)
    # pass it to another function to return an array 248/8 show the avg error
    # print(len(answer))
    plotter(len(answer),answer,"Average error within a symbol over all packet","symbol index","avg number of error",0,len(answer),0,0.7)

def plotBitErrorNumberForEachGeneration(list):
    '''
    receives  lists of  error indicies over all generations and calculates
    the avg number of error ( in bits ) for all received error patterns
    '''
    NumberOfBitErrorForEachGeneration = []
    sum = 0 
    for InnerListOfErrorIndicies in list:
        NumberOfBitErrorForEachGeneration.append(len(InnerListOfErrorIndicies))
        sum +=len(InnerListOfErrorIndicies)

    answer = NumberOfBitErrorForEachGeneration
    print("The average is ", float(sum)/float(len(NumberOfBitErrorForEachGeneration)))
    plotter(len(answer),answer,"Bit Error within a Received error pattern","Received Packet Index","#error",0,len(answer),0,50)
    
def errorCorrectionPercentageForDifferentMDSCodes(list):
    '''
    Returns how much (percentage) of packets could be corrected with MDS code 
    with different errorCorrectionCapabilities
    '''
    numberOfErrorDistributionOverAllReceivedPacket = [ 0 for i in range(8*31)]
    for InnerListOfErrorIndicies in list:
        numberOfErrorDistributionOverAllReceivedPacket[len(InnerListOfErrorIndicies)] +=1

    CDF = [ 0 for i in range(8*31)]

    CDF[0] = numberOfErrorDistributionOverAllReceivedPacket[0]
    for i in range(1,len(numberOfErrorDistributionOverAllReceivedPacket)):
        CDF[i] = CDF[i-1] + numberOfErrorDistributionOverAllReceivedPacket[i] 

    # percentage
    for i in range(len(CDF)):
        CDF[i] = (CDF[i] / len(list))*100
    print(numberOfErrorDistributionOverAllReceivedPacket)
    answer = CDF
    plotter(len(answer),answer,"Relation between % of the corrected packets with the MDS error correction Rate ","MDS error correction","%Correction",0,50,0,100)

def errorCorrectionNumberForDifferentMDSCodes(list):
    '''
    Returns how much (number) of packets could be corrected with MDS code 
    with different errorCorrectionCapabilities
    '''
    numberOfErrorDistributionOverAllReceivedPacket = [ 0 for i in range(8*31)]
    for InnerListOfErrorIndicies in list:
        numberOfErrorDistributionOverAllReceivedPacket[len(InnerListOfErrorIndicies)] +=1

    CDF = [ 0 for i in range(8*31)]

    CDF[0] = numberOfErrorDistributionOverAllReceivedPacket[0]
    for i in range(1,len(numberOfErrorDistributionOverAllReceivedPacket)):
        CDF[i] = CDF[i-1] + numberOfErrorDistributionOverAllReceivedPacket[i] 


    print(numberOfErrorDistributionOverAllReceivedPacket)
    answer = CDF
    plotter(len(answer),answer,"Relation between # of the corrected packets with the MDS correction Rate ","MDS error correction rate","#Correction",0,50,0,6100)

    